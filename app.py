from flask import Flask, request


app = Flask(__name__)


@app.route("/hi/<username>/")
def index(username):
    pass

@app.route("/a/<int:a>/<int:b>/")
def int_a(a, b):

    print(a, b)

    return f"<h1>hi, {a}, {b}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
