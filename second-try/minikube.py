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

@app.route("/activatescripts/", methods=['GET', 'POST'])
def activatescripts():
   subprocess.call(['./activatescripts.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/startminikube/", methods=['GET', 'POST'])
def startminikube():
   subprocess.call(['./startminikube.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/minikubedashboard/", methods=['GET', 'POST'])
def minikubedashboard():
  subprocess.call(['./minikubedashboard.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

@app.route("/stopminikube/", methods=['GET', 'POST'])
def stopminikube():
  subprocess.call(['./stopminikube.sh'], shell=True)
  #return render_template("main.html")
  return redirect('http://127.0.0.1:5000/')

if __name__ == "__main__":
   app.run(port=5000, debug=True)
