# Sports Chatbot

A simple Sports Chatbot built with Python Flask.

## Project Structure

```text
sports_chatbot/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Technologies

- Python
- Flask
- HTML
- CSS
- JavaScript
- python-dotenv
- Gunicorn

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:
http://127.0.0.1:5000

## Run with Gunicorn

```bash
gunicorn app:app
```

For a specific port:

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

## Example Questions

- Tell me about cricket
- What is football?
- Explain basketball
- What is tennis?
- Tell me about badminton
