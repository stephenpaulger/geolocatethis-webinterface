from flask import Flask
from secrets import token_hex

app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(16)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
