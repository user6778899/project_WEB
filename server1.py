from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "«Сайт помощник для тех, кто оканчивает 11 класс»"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


# http://127.0.0.1:8080/
