from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Python Flask'

@app.route('/hello/<string:name>')
def helloIndex(name):
	return 'Hello World from ' + name + ' !'

app.run(host='0.0.0.0', port= 6050)