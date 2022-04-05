from flask import Flask
from jinja2 import FileSystemLoader, Environment

app = Flask(__name__, template_folder='template')

f = FileSystemLoader('templates')
env = Environment(loader=f)

tm = env.get_template('index.html')
msg = tm.render()


@app.route('/')
def hello():
    return msg


if __name__ == "__main__":
    app.run()
