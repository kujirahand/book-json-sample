from flask import Flask, request, send_file
import joblib
app = Flask(__name__)
clf = joblib.load('images/numimage.model')

@app.route('/')
def index():
    return send_file('numimage_test.html')

@app.route('/api')
def api():
    q = request.args.get('q', '')
    if q == '': return '?'
    q_list = list(map(lambda v:int(v)*255, list(q)))
    print(q_list)
    r_list = clf.predict([q_list[0:28*28]])
    return str(r_list[0])

if __name__ == '__main__':
    app.run('0.0.0.0', 8888, debug=True)

