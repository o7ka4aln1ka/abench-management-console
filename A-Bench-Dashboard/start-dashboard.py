# main script for starting the webui

from flask import Flask, render_template, redirect
import subprocess
from subprocess import Popen, PIPE
import os
import datetime
import time
import pandas as pd

app = Flask(__name__)

cpu_colnames=['time', 'value']
cpu_data = pd.read_csv('/home/vr/BigBench2-easy-deploy/cpu_usage_A_I_K.csv', skiprows=[0], names=cpu_colnames)
cpu_labels = cpu_data.time.tolist()
cpu_values = cpu_data.value.tolist()

mem_colnames=['time', 'value']
mem_data = pd.read_csv('/home/vr/BigBench2-easy-deploy/memory_usage_A_I_K.csv', skiprows=[0], names=mem_colnames)
mem_labels = mem_data.time.tolist()
mem_values = mem_data.value.tolist()

file_colnames=['time', 'value']
file_data = pd.read_csv('/home/vr/BigBench2-easy-deploy/filesystem_usage_A_J_L.csv', skiprows=[0], names=file_colnames)
file_labels = file_data.time.tolist()
file_values = file_data.value.tolist()

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route("/", methods=['GET', 'POST'])
def home():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M %d-%m-%Y")
   templateData = {
      'title' : 'A-Bench',
      'time': timeString
      }
   return render_template('homepage.html', **templateData)

@app.route("/activateScripts/", methods=['GET', 'POST'])
def activateScripts():
   subprocess.call(['./activatescripts.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/checkPreRequirements/", methods=['GET', 'POST'])
def checkPreRequirements():
   subprocess.call(['./pre-requirements.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

# generate CSVs
@app.route("/csv_from_excel/", methods=['GET', 'POST'])
def csv_from_excel():
   subprocess.Popen(['./csv_from_excel.py'], shell=True)
   return redirect('http://127.0.0.1:5000/')

# generate CONFIG file
@app.route("/config_txt/", methods=['GET', 'POST'])
def config_txt():
   subprocess.Popen(['./create_txt_config.py'], shell=True)
   return redirect('http://127.0.0.1:5000/config')

# choose which queries to run
@app.route("/query1/", methods=['GET', 'POST'])
def query1():
   subprocess.Popen(['/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/queries/query1.py'], shell=True)
   return redirect('http://127.0.0.1:5000/config')

@app.route("/query2/", methods=['GET', 'POST'])
def query2():
   subprocess.Popen(['/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/queries/query2.py'], shell=True)
   return redirect('http://127.0.0.1:5000/config')

@app.route("/query3/", methods=['GET', 'POST'])
def query3():
   subprocess.Popen(['/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/queries/query3.py'], shell=True)
   return redirect('http://127.0.0.1:5000/config')

@app.route("/query4/", methods=['GET', 'POST'])
def query4():
   subprocess.Popen(['/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/queries/query4.py'], shell=True)
   return redirect('http://127.0.0.1:5000/config')

@app.route("/query5/", methods=['GET', 'POST'])
def query5():
   subprocess.Popen(['/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/queries/query5.py'], shell=True)
   return redirect('http://127.0.0.1:5000/config')

# create the infrastructure
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

@app.route("/config/", methods=['GET', 'POST'])
def config():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M %d-%m-%Y")
   templateData = {
      'title' : 'A-Bench',
      'time': timeString
      }
   return render_template('config.html', **templateData)

@app.route('/barCPUusage')
def bar():
    bar_labels=cpu_labels
    bar_values=cpu_values
    return render_template('CPU_Usage_Chart.html', title='CPU Usage', max=2095640174197, labels=bar_labels, values=bar_values)

@app.route('/barMemoryUsage')
def barMemoryUsage():
    bar_labels=mem_labels
    bar_values=mem_values
    return render_template('Memory_Usage_Chart.html', title='Memory Usage', max=7388910336, labels=bar_labels, values=bar_values)

@app.route('/barFilesystemUsage')
def barFilesystemUsage():
    bar_labels=file_labels
    bar_values=file_values
    return render_template('Filesystem_Usage_Chart.html', title='Filesystem Usage', max=3610571264, labels=bar_labels, values=bar_values)

@app.route('/densityGraph')
def densityGraph():
    return render_template('density_d3_graph.html')

@app.route('/zoomDotGraph')
def zoomDotGraph():
    return render_template('zoom_d3_dots.html')

if __name__ == "__main__":
   app.run(port=5000, debug=True, use_reloader=False)
