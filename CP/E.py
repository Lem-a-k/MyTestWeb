# flask
# sqlite
import json

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/test')
def server_test():
    # ... обращение к базе
    with open('...') as file:
        pass
    res = [{'x': 2}]
    return jsonify(res)  # json.dumps(res)   # {'test': [1, 2, 3]}


if __name__ == "__main__":
    app.run(port=5000, host='127.0.0.1')
