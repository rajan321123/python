from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Predefined responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase?",
}

# Function to match user input with a response
def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if re.search(rf"\b{key}\b", user_input):
            return responses[key]
    return responses["default"]

# Chatbot route
@app.route("/", methods=["GET", "POST"])
def chatbot_view():
    response = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        response = chatbot_response(user_input)
    return render_template("chatbot.html", response=response, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
