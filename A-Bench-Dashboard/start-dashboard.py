from flask import Flask, render_template, redirect
import subprocess
import os
import datetime
import time
import pandas as pd

app = Flask(__name__)

colnames=['time', 'value']
data = pd.read_csv('/home/vr/BigBench2-easy-deploy/cpu_usage_A_I_K.csv', skiprows=[0], names=colnames)
labels = data.time.tolist()
values = data.value.tolist()

# labels = [
#     'JAN', 'FEB', 'MAR', 'APR',
#     'MAY', 'JUN', 'JUL', 'AUG',
#     'SEP', 'OCT', 'NOV', 'DEC'
# ]

# values = [
#     967.67, 1190.89, 1079.75, 1349.19,
#     2328.91, 2504.28, 2873.83, 4764.87,
#     4349.29, 6458.30, 9907, 16297
# ]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route("/", methods=['GET', 'POST'])
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M %d-%m-%Y")
   templateData = {
      'title' : 'A-Bench',
      'time': timeString
      }
   return render_template('main.html', **templateData)
   # return render_template('test.html', **templateData)

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

@app.route("/startPromethius/", methods=['GET', 'POST'])
def startPromethius():
  subprocess.call(['./startpromethius.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='CPE Usage', max=565640174197, labels=bar_labels, values=bar_values)


if __name__ == "__main__":
   app.run(port=5000, debug=True, use_reloader=False)
