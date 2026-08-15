import flask

app = flask.Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
  return "hillohoi " + name



@app.route('/')
def home():


    completed = False
    return flask.render_template('index.html', completed = completed)

app.run(debug=True)