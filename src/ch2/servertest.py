from flask import Flask, request, redirect
app = Flask(__name__) # Flaskを生成
val = 30

@app.route('/')
def index():
    global val
    return "@=" + str(val)

@app.route('/change')
def change():
    global val
    val += 1
    return redirect('/')

app.run('127.0.0.1', 8888, debug=True)

