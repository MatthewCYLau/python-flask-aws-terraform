from app import app


@app.route("/ping")
def ping():

    return "pong!"
