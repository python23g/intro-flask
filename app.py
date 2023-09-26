from flask import Flask, request, render_template
import requests


app = Flask(__name__)


def get_users(n: int):
    url = 'https://randomuser.me/api/'
    payload = {
        'results': n
    }

    r = requests.get(url, params=payload)

    users = []
    n = 1
    for user in r.json()['results']:
        users.append({
            'id': n,
            'first': user['name']['first'],
            'last': user['name']['last'],
            'age': user['dob']['age'],
            'gender': user['gender'],
            'email': user['email'],
            'location': user['location']['country'],
            'link': user['picture']['large'],
        })
        n += 1

    return users


@app.route("/users")
def index():
    title = 'Random Users'

    n = request.args.get('n', 1)

    context = {
        'title': title,
        'users': get_users(int(n))
    }

    return render_template('index.html', context=context)


if __name__ == "__main__":
    app.run(debug=True)
