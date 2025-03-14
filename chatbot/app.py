import secrets
from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai

app = Flask(__name__)

# Generate a secure random secret key
app.secret_key = secrets.token_hex(16)  

# Initialize Gemini AI Client
genai.configure(api_key="")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")  # Correct model

def get_gemini_response(prompt, history):
    """Generate AI response while handling empty outputs properly."""
    
    full_prompt = "\n".join(history + [prompt])  # Maintain history

    try:
        response = model.generate_content(full_prompt)

        if response.text:  
            return response.text.replace("**", "").strip()
        else:
            return "Sorry, I can't generate a response for this input."

    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=['POST', 'GET'])
def chatbot():
    if 'history' not in session:
        session['history'] = []  # Initialize chat history

    if request.method == 'POST':
        prompt = request.form['prompt'].strip()

        if not prompt:  
            return jsonify({'response': "Please enter a message."})

        history = session['history'][-5:]  # Limit chat history
        
        response = get_gemini_response(prompt, history)

        session['history'].append(f"User: {prompt}")
        session['history'].append(f"Bot: {response}")

        session.modified = True  
        return jsonify({'response': response})

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
