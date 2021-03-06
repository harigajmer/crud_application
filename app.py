import imp
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, host = 'localhost', port="9000")