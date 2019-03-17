from flask import Flask, render_template, redirect
import subprocess
import os
import datetime
import time
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'BigBench2',
      'time': timeString
      }
   return render_template('main.html', **templateData)

@app.route("/activateScripts/", methods=['GET', 'POST'])
def activateScripts():
   subprocess.call(['./activatescripts.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/checkPreRequirements/", methods=['GET', 'POST'])
def checkPreRequirements():
   subprocess.call(['./pre-requirements.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/prep-start-spark/", methods=['GET', 'POST'])
def prepStartSpark():
   subprocess.call(['./prep-start-spark.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/startMinikube/", methods=['GET', 'POST'])
def startMinikube():
   subprocess.call(['./startminikube.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/minikubedashboard/", methods=['GET', 'POST'])
def minikubeDashboard():
  subprocess.call(['./minikubeDashboard.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

@app.route("/stopMinikube/", methods=['GET', 'POST'])
def stopMinikube():
  subprocess.call(['./stopminikube.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

if __name__ == "__main__":
   app.run(port=5000, debug=True)
