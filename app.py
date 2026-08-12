import flask

app = flask.Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
  return "hillohoi " + name


@app.route('/')
def home():
  return "Task Manager"

app.run(debug=True)