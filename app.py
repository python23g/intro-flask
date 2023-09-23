from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return '''<form action="http://127.0.0.1:5000/form">
            <label>a:</label><br>
            <input type="text"  name="a" value="0"><br>
            <label>b:</label><br>
            <input type="text" name="b" value="0"><br><br>
            <label>operate:</label><br>
            <input type="text" name="op" value="+"><br><br>
            <input type="submit" value="Submit">
            </form>'''

@app.route("/form")
def news():

    params = request.args

    # get a and b
    a = params.get('a')
    b = params.get('b')

    # get op
    op = params.get('op')

    if op == "+":
        return f"<h1>{a} + {b} = {int(a) + int(b)}</h1>"

    if op == "-":
        return f"<h1>{a} - {b} = {int(a) - int(b)}</h1>"

    if op == "*":
        return f"<h1>{a} * {b} = {int(a) * int(b)}</h1>"

    if op == "/":
        if int(b) == 0:
            return "can not divide by 0."
        return f"<h1>{a} / {b} = {round(int(a) / int(b), 2)}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
