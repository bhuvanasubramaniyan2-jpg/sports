import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SPORTS_KNOWLEDGE = {
    "football": "Football is a team sport played between two teams of 11 players. The objective is to score more goals than the opponent.",
    "cricket": "Cricket is played between two teams, usually with 11 players each. Common formats include Test, ODI and T20.",
    "basketball": "Basketball is played by two teams of five players. Teams score by shooting the ball through the opponent's hoop.",
    "tennis": "Tennis is played in singles or doubles. Players use a racket to hit a ball over a net and win points, games and sets.",
    "badminton": "Badminton can be played in singles or doubles. Players use rackets to hit a shuttlecock over a net.",
}

def sports_reply(message):
    text = message.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 I am your Sports Chatbot. Ask me about football, cricket, basketball, tennis or badminton."

    for sport, description in SPORTS_KNOWLEDGE.items():
        if sport in text:
            return description

    if "sport" in text:
        return "Sports include football, cricket, basketball, tennis, badminton, volleyball and many more. Ask me about a specific sport!"

    return "I can answer basic sports questions. Try asking: 'Tell me about cricket', 'What is football?', or 'Explain basketball'."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    if not message:
        return jsonify({"reply": "Please enter a question."}), 400
    return jsonify({"reply": sports_reply(message)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
