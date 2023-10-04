from flask import flask

app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'hello world!'
if __name__ == '__main__':
    app.run(port = '0.0.0.0', host = 80100, debug = True)
