from api import app


def runserver():
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)


if __name__ == "__main__":
    runserver()
