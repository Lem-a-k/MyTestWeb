from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main_page():
    return "<h1>Привет, Яндекс!</h1><br />Ура!"


@app.route('/second')
def second_page():
    return """Second <p>page</p>
1
<div>2</div>"""


@app.route('/image_sample')
def image():
    return f'''<img width=500pt src="{url_for('static', filename='img/owl.jpeg')}" 
           alt="та самая сова">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
