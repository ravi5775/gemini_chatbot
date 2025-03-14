1. Create and Activate Virtual Environment
For Windows (cmd/Powerell):

python -m venv myenv
myenv\Scripts\activate

For Linux/macOS (ba/z):

python3 -m venv myenv
source myenv/bin/activate



2. Install Required Packages

pip install flask google-generativeai



3. Set Up and Run the Flask App
For Windows (cmd/Powerell):

set FLASK_APP=app.py
set FLASK_ENV=development
flask run


For Linux/macOS (ba/z):

export FLASK_APP=app.py
export FLASK_ENV=development
flask run

4. Open the Chatbot
Once the server starts, open your browser and go to:
cpp


http://127.0.0.1:5000

for api : https://aistudio.google.com/prompts/new_chat or https://ai.google.dev/ 
