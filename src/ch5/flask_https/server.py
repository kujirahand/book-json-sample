from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello</h1>'

if __name__ == '__main__':
    app.run('0.0.0.0', 8888)

