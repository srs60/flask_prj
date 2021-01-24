from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def index(name):
    return render_template("hello.html",name=name)

app.run(host='0.0.0.0', port= 6050)
