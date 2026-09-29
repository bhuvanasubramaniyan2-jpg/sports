import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Sports Chatbot")
PORT = int(os.getenv("PORT", "5000"))
