import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return f'Hello {os.getenv("APP_NAME")}'


@app.route("/ping")
def ping():
    return "pong!"

if __name__ == "__main__":
    app.run(debug=True)