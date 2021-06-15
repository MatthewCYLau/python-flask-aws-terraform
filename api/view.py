from api import app


@app.route("/ping")
def ping():

    return "pong!"
