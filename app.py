import flask

app = flask.Flask(__name__)

@app.route('/hello/<name>')
def home(name):
  return "hello" + name

app.run()