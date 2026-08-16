import flask
from flask_sqlalchemy import SQLAlchemy

#sqllite

app = flask.Flask(__name__)

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"]  = "sqlite:///database.db"

db.init_app(app)

class Task(db.Model):
   __tablename__ = "Tasks"

   id = db.Column(db.Integer, primary_key = True)
   title = db.Column(db.String)
   description = db.Column(db.String)
   completed = db.Column(db.Boolean)


with app.app_context():
   db.create_all()

@app.route('/hello/<name>')
def hello(name):
  return "hillohoi " + name



@app.route('/')
def home():


    completed = False
    return flask.render_template('index.html', completed = completed)

app.run(debug=True)