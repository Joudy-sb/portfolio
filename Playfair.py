class EncryptPF:
    def __init__(self,text, word1, word2):
        self.text = text
        self.word1 = word1
        self.word2 = word2
        self.matrix1 = self.generate_matrix(self.word1)
        self.matrix2 = self.generate_matrix(self.word2)

    @staticmethod
    def generate_matrix(word):
        alphabet = 'abcdefghiklmnopqrstuvwxyz'  # excluding 'j' to avoid repeating letters
        matrix = []
        
        # Remove 'j' from the given word
        word = word.replace('j', 'i')
        
        # Add unique characters from the word to the matrix
        for char in word:
            if char not in matrix:
                matrix.append(char)
        
        # Add remaining characters from the alphabet to complete the matrix
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)
        
        # Reshape the list into a 5x5 matrix
        matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        
        return matrix
    
    @staticmethod
    def find_indices(matrix, char):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == char:
                    return i, j
        return None
       
    def preserve_special_char(self,plaintext):
        special_char = []
        preserved_text = ""
        for i in range(0,len(plaintext)):
            if plaintext[i].isalpha()!=True:
                special_char.append((plaintext[i],i))
            else:
                preserved_text += plaintext[i]
        return (preserved_text, special_char)

    def add_preserved_special_char(self,ciphertext, special_char):
        ciphertext = list(ciphertext)
        for i in special_char: 
            ciphertext.insert(i[1],i[0])
        return ''.join(ciphertext)

    
    def playfair_encrypt(self):
        ciphertext = ""
        preserved_text, special_char = self.preserve_special_char(self.text)
        preserved_text= preserved_text.lower()
        
        for i in range(0, len(preserved_text), 2):
            char1, char2 = preserved_text[i], 'x' if i+1 == len(preserved_text) else preserved_text[i+1]
            char1n= char1
            char2n= char2
            if char1 == 'j':
                char1n = 'i'
            if char2 == 'j':
                char2n = 'i'

            row1_m1, col1_m1 = self.find_indices(self.matrix1, char1n)
            row2_m2, col2_m2 = self.find_indices(self.matrix2, char2n)
            
            if col1_m1 == col2_m2:
                # If both characters are in the same column, take the characters as is
                encrypted_char1 = char1
                encrypted_char2 = char2
            else:
                # If the characters are not in the same column, use the rules of Playfair cipher
                encrypted_char1 = self.matrix1[row1_m1][col2_m2]
                encrypted_char2 = self.matrix2[row2_m2][col1_m1]
            
            ciphertext += encrypted_char1 + encrypted_char2
        ciphertext = self.add_preserved_special_char(ciphertext, special_char)

        return ''.join(ciphertext)

    
    def playfair_decrypt(self):
        plaintext = ""
        preserved_text, special_char = self.preserve_special_char(self.text)
        preserved_text= preserved_text.lower()

        for i in range(0, len(preserved_text), 2):
            char1, char2 = preserved_text[i], preserved_text[i+1]
            char1n= char1
            char2n= char2
            if char1 == 'j':
                char1n = 'i'
            if char2 == 'j':
                char2n = 'i'

            row1_m1, col1_m1 = self.find_indices(self.matrix1, char1n)
            row2_m2, col2_m2 = self.find_indices(self.matrix2, char2n)
            
            if col1_m1 == col2_m2:
                decrypted_char1 = char1
                decrypted_char2 = char2
            else:
                decrypted_char1 = self.matrix1[row1_m1][col2_m2]
                decrypted_char2 = self.matrix2[row2_m2][col1_m1]

            plaintext += decrypted_char1 + decrypted_char2
        plaintext = self.add_preserved_special_char(plaintext, special_char)

        return ''.join(plaintext)




'''
def main():
    choice = input("Do you want to encrypt or decrypt? Enter 'encrypt' or 'decrypt': ")

    if choice == 'encrypt':
        word1 = input("Enter first word: ")
        word2 = input("Enter second word: ")
        plaintext = input("Enter the plaintext message: ")

        matrix1 = generate_matrix(word1)
        matrix2 = generate_matrix(word2)

        encrypted_text = playfair_encrypt(plaintext, matrix1, matrix2)
        print("Encrypted Text:", encrypted_text)

    elif choice == 'decrypt':
        word1 = input("Enter first word: ")
        word2 = input("Enter second word: ")
        ciphertext = input("Enter the ciphertext message: ")

        matrix1 = generate_matrix(word1)
        matrix2 = generate_matrix(word2)

        decrypted_text = playfair_decrypt(ciphertext, matrix1, matrix2)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
'''