from flask import Flask, jsonify, redirect, render_template, request, session, url_for
import random
from string import ascii_uppercase
from HillCipher import EncryptHC
from Playfair import EncryptPF
from EEA import eea
import numpy as np 
from flask_socketio import SocketIO, emit, leave_room, send, join_room

from HillCipher import EncryptHC

app = Flask(__name__)
app.config["SECRET_KEY"] = "line&joods"
socketio = SocketIO(app)

room_users = {}
room_keys = set()
message_history = {}

def generate_key():
    while True: 
        key = ""
        for i in range(0,4):
            key += random.choice(ascii_uppercase)
        if key not in room_keys:
            room_keys.add(key)
            break
    return key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatroom')
def chatroom():
    return render_template('chatroom.html')

@app.route('/chatroom/create_room')
def create_room():
    return render_template('create_room.html')

@app.route("/chatroom/room")
def room():
    room_key = session.get("room")
    user_name = session.get("name")

    if room_key is None or user_name is None or room_key not in room_keys:
        return redirect(url_for("chatroom"))
    
    return render_template("room.html", room_key=room_key, messages=message_history[room_key])

@app.route('/chatroom/process_create_room', methods=['POST'])
def process_create_room():
    user_name = request.form['name']
    room_key = generate_key() # automatically add the room key to list of keys

    session["name"] = user_name
    session["room"] = room_key

    # create a room key and store the members in the room
    room_users.setdefault(room_key, []).append(user_name)

    # create a message history 
    if room_key not in message_history:
        message_history[room_key] = []

    return redirect(url_for("room"))

@app.route('/chatroom/join_room')
def join_room_view():
    return render_template('join_room.html')

@app.route('/chatroom/process_join_room', methods=['POST'])
def process_join_room():
    user_name = request.form['name']
    room_key = request.form['key']

    if room_key not in room_keys:
        return render_template('join_room.html', error='Room does not exist.')
    
    # add user to the room
    room_users[room_key].append(user_name)
    
    session["room"] = room_key
    session["name"] = user_name
    
    return redirect(url_for("room"))

@socketio.on('connect')
def connect(auth):
    user_name = session.get('name')
    room_key = session.get('room')

    # an error in the session information
    if not user_name or not room_key:
        return  

    # if room does no exist, error
    if room_key not in room_keys:
        leave_room(room_key)
        return 

    join_room(room=room_key)

    send({"name": user_name, "message": "has entered the room"}, to=room_key)

    print(f"{user_name} joined room {room_key}")

@socketio.on('disconnect')
def disconnect():
    user_name = session.get("name")
    room_key = session.get("room")
    leave_room(room_key)

    # Check if room_key exists in room_users dictionary
    if room_key and room_key in room_users:

        # Perform action with room_users[room_key]
        if user_name in room_users[room_key]:
            room_users[room_key].remove(user_name)

            # if there are no more users
            if not room_users[room_key]:
                del room_users[room_key]
                room_keys.remove(room_key)

        send({"name": user_name, "message": "has left the room"}, room=room_key)
        print(f"{user_name} left room {room_key}")
    else:
        print(f"Attempted to disconnect from an unknown room {room_key}")


@socketio.on('message')
def message(data):
    user_name = session.get("name")
    room_key = session.get("room")

    if room_key not in room_keys:
        return False
    
    user_key = [[7, 3], [2, 5]]
    
    cipher = EncryptHC(data['data'], user_key, 26)
    ciphertext = cipher.encrypt(data['data'])

    content = {
        "name": user_name,
        "message": str(ciphertext)
    }
    
    # append messages sent to history
    message_history[room_key].append(content)

    send(content, to=room_key)

    print(f"{user_name} said: {data['data']}")

@socketio.on('decrypt')
def decrypt(data):
    user_name = session.get("name")
    room_key = session.get("room")

    if room_key not in room_keys:
        return False
    
    user_key = [[7, 3], [2, 5]]
    
    cipher = EncryptHC(data['data'], user_key, 26)
    ciphertext = cipher.decrypt(data['data'])

    content = {
        "name": "Decrypted",
        "message": str(ciphertext)
    }
    
    # Send the decrypted message only to the client who requested it
    emit('message', content, room=request.sid)

    print(f"{user_name} said: {data['data']}")


@app.route('/cryptool')
def cryptool():
    title = 'Choose your cipher'
    return render_template('cryptool.html', title=title)

@app.route('/cryptool/hillcipher')
def hillcipher():
    return render_template('hillcipher.html')

@app.route('/cryptool/playfaircipher')
def playfaircipher():
    return render_template('playfaircipher.html')

@app.route('/cryptool/eea')
def extendedeuclidalgo():
    return render_template('eea.html')

@app.route('/cryptool/process_hillcipherEN', methods=['POST'])
def process_hillcipherEN():
    user_message = request.form['message']
    user_key = request.form['key']
    rows = user_key.strip('{}').split('},{')
    user_key = [[int(e) for e in row.split(',')] for row in rows]
    user_mod = int(request.form['mod'])
    cipher = EncryptHC(user_message, user_key, user_mod)
    ciphertext = cipher.encrypt(user_message)
    return render_template('hillcipher.html', ciphertext=ciphertext)

@app.route('/cryptool/process_hillcipherDC', methods=['POST'])
def process_hillcipherDC():
    user_message = request.form['message']
    user_key = request.form['key']
    rows = user_key.strip('{}').split('},{')
    user_key = [[int(e) for e in row.split(',')] for row in rows]
    user_mod = int(request.form['mod'])
    cipher = EncryptHC(user_message, user_key, user_mod)
    plaintext = cipher.decrypt(user_message)
    return render_template('hillcipher.html', plaintext=plaintext)

@app.route('/cryptool/process_eea', methods=['POST'])
def process_eea():
    user_b = int(request.form['b'])
    user_m = int(request.form['m'])
    obj = eea(user_b,user_m)
    inverse = obj.findinverse()
    return render_template('eea.html', user_b=user_b, user_m=user_m, inverse=inverse)


@app.route('/cryptool/process_playfaircipherEC', methods=['POST'])
def process_playfaircipherEC():
    user_message = request.form['message']
    key1 = request.form['key1']
    key2 = request.form['key2']
    
    playfair_cipher = EncryptPF(user_message, key1, key2)
    ciphertext = playfair_cipher.playfair_encrypt()
    
    return render_template('playfaircipher.html', ciphertext=ciphertext)

@app.route('/cryptool/process_playfaircipherDC', methods=['POST'])
def process_playfaircipherDC():
    user_message = request.form['message']
    key1 = request.form['key1']
    key2 = request.form['key2']
    
    playfair_cipher = EncryptPF(user_message, key1, key2)
    plaintext = playfair_cipher.playfair_decrypt()
    
    return render_template('playfaircipher.html', plaintext=plaintext)


@app.route('/readings')
def readings():
    return render_template('readings.html')


if __name__ == "__main__":
    socketio.run(app, debug=True)