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
   # task = Task(
   #    title = "omar",
   #    description = "nothing",
   #    completed = True
   # )
   # db.session.add(task)
   # db.session.commit()

   # tasks = Task.query.all()
   # for task in tasks:
   #  print(task.description)

  
@app.route('/hello/<name>')
def hello(name):
  return "hillohoi " + name



@app.route('/', methods=["GET", "POST"])
def home():
    if flask.request.method == "POST":
       print(flask.request.form)
       title = flask.request.form["title"]
       description = flask.request.form["description"]
       completed = flask.request.form.get("completed") == "True"


       task = Task(
           title=title,
           description=description,
           completed=completed
       )
       db.session.add(task)
       db.session.commit()
      
       
    return flask.render_template('index.html',  tasks = Task.query.all() )

app.run(debug=True)

