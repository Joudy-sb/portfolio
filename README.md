Portfolio Website
This is a Python-based website that you can run locally using Flask.

Requirements
Before running the project, make sure you have all the necessary dependencies installed. The dependencies are listed in the requirements.txt file.

Prerequisites
Python 3.x
Virtual Environment (optional but recommended)
Setup
Step 1: Clone the repository
bash
Copy code
git clone <repository-url>
cd <repository-directory>
Step 2: Create and activate a virtual environment (optional)
To avoid conflicts with other Python projects, it's recommended to use a virtual environment.

bash
Copy code
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
Step 3: Install the dependencies
Once the virtual environment is activated (if you're using one), install the required packages.

bash
Copy code
pip install -r requirements.txt
Step 4: Run the website
After all dependencies are installed, you can run the app by executing the following command:

bash
Copy code
python app.py
The website will be available at http://127.0.0.1:5000/ by default.
