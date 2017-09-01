from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
#from flask.ext.sqlalchemy import SQLAlchemy
#from flask_script import Manager
#from flask_migrate import Migrate, MigrateCommand
from final import *
import os
import plotly as py

# app configuration
app = Flask(__name__)
#db_path = os.path.join(os.path.dirname(__file__), 'app.db')
#db_uri = 'sqlite:///{}'.format(db_path)
#app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tmp/test.db"
app.debug = True
# db configuration
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

#manager = Manager(app)
#manager.add_command("db", MigrateCommand)
dorms = {"1": "Morewood", "2": "Stever", "3": "Mudge", "4": "Donner", "5": "Boss", "6": "Schlag", "7": "Scobel", "8": "Other"}
students = set()
currStudent = None
sickDorms = dict()
sickType = dict()
sickPerDay = []
def getSampleData():
    global sickDorms
    global sickType
    global sickPerDay
    
    sickDorms=dict()
    sickDorms["Hill"]=16
    sickDorms["Donner"]=9
    sickDorms["Morewood"]=5
    sickDorms["Stever"]=7
    sickDorms["Mudge"]=9
    sickDorms["RezShir"]=3
    sickDorms["Other"]=147
    
    sickType=dict()
    sickType["Cold"]=30
    sickType["Fever"]=10
    sickType["Flu"]=5
    sickType["Other"]=4
    sickType["Healthy"]=772

    sickPerDay=[((2016,1,23),45),((2016,1,24),47),((2016,1,25),50),((2016,1,26),48),((2016,1,27),55),((2016,1,28),52),
    ((2016,1,29),53),((2016,1,30),53),((2016,1,31),59),((2016,2,1),56),((2016,2,2),52),((2016,2,3),50),((2016,2,4),51),((2016,2,5),44),((2016,2,6),49)]
getSampleData()
# routing
@app.route("/")
def home():
  return render_template("index.html")

@app.route("/user")
def user():
  writeFile("static/sick5.txt", getContents())
  #makeGraphTimeline(sickPerDay)
  return render_template("user.html")

@app.route("/check1")
def check1():
  return render_template("check1.html")

@app.route("/check2")
def check2():
  return render_template("check2.html")

@app.route("/register")
def register():
  return render_template("register.html")

@app.route("/userPersonal")
def userPersonal():
  #makeGraphTimeline(sickPerDay)
  return render_template("userPersonal.html")

@app.route("/userDorm")
def userDorm():
  #makeBarChart(sickDorms)
  return render_template("userDorm.html")

@app.route("/userType")
def userType():
  #makePieChart(sickType)
  #makePieChart2(sickType)
  return render_template("userType.html")

@app.route("/login" , methods = ["POST"])
def login():
  ID = request.form["andrewid"]
  global students
  if Student(ID, None) in students: return redirect(url_for("check2"))
  else: return render_template("index.html")

@app.route("/newpost", methods=["POST"])
def newpost():
  andrewid = request.form["post-name"]
  dorm = request.form["post-title"]
  # case invalid
  if not validate(andrewid):
    return render_template("register.html")
  # success, commit to database
  else:
    global currStudent
    currStudent = Student(andrewid, dorm)
    students.add(currStudent)
    return redirect(url_for("check1"))

@app.route("/checkType", methods = ["POST"])
def checkType():
  response = [False] * 4
  formData = request.form["check"]
  global currStudent
  updateSickness(currStudent, "cold")
  #response = "Form Contents <pre>%s</pre>" % "<br/>\n".join(["%s:%s" % item for item in formData.items()] )
  return redirect(url_for("user"))

@app.route("/sickness")
def sickness():
  return render_template("sickness.html")

# actual calls
if __name__ == "__main__":
  app.run()
