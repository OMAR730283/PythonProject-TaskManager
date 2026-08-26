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
   # task = Task.query.get(1)
   # task.title = "omar faruk"
   # print(task.title)
   # db.session.commit()

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


@app.route('/update/<int:id>', methods=["GET", "POST"])

def update(id):
  task = Task.query.get(id)
  if not task:
     return "id not found"
  if flask.request.method == "POST":
        task.title = flask.request.form["title"]
        task.description = flask.request.form["description"]
        task.completed = flask.request.form.get("completed") == "True"

        db.session.commit()

  return flask.render_template("update.html", task=task)

@app.route('/delete/<int:id>', methods = ["POST"])

def delete(id):
   task = Task.query.get(id)
   if not task:
      return "id not found"
   db.session.delete(task)   
   db.session.commit()
   return flask.redirect(flask.url_for("home"))
 
app.run(debug=True)

