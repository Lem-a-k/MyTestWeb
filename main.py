from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main_page():
    return "<h1>Привет, Яндекс!</h1>"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')