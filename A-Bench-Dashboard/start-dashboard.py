# main script for starting the webui

from flask import Flask, render_template, redirect
import subprocess
from subprocess import Popen, PIPE
import os
import datetime
import time
import pandas as pd
import json
import csv

app = Flask(__name__)

cpu_colnames=['time', 'value']
cpu_data = pd.read_fwf("/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/future-app/a-bench/results/20190519_11_39_26/experiment_results/cpu_usage.txt", header=0, usecols=cpu_colnames, engine='python')
cpu_labels = cpu_data.time.tolist()
cpu_values = cpu_data.value.tolist()

# cpu_colnames=['time', 'value']
# cpu_data = pd.read_csv('/home/vr/BigBench2-easy-deploy/cpu_usage_A_I_K_short.csv', skiprows=[0], names=cpu_colnames)
# cpu_labels = cpu_data.time.tolist()
# cpu_values = cpu_data.value.tolist()

mem_colnames=['time', 'value']
mem_data = pd.read_fwf("/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/future-app/a-bench/results/20190519_11_39_26/experiment_results/memory_usage.txt", header=0, usecols=mem_colnames, engine='python')
mem_labels = mem_data.time.tolist()
mem_values = mem_data.value.tolist()

file_colnames=['time', 'value']
file_data = pd.read_fwf("/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/future-app/a-bench/results/20190519_11_39_26/experiment_results/filesystem_usage.txt", header=0, usecols=file_colnames, engine='python')
file_labels = file_data.time.tolist()
file_values = file_data.value.tolist()


@app.route("/", methods=['GET', 'POST'])
def home():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M %d-%m-%Y")
   templateData = {
      'title' : 'A-Bench',
      'time': timeString
      }
   text = open('/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/output.txt', 'r+')
   content = text.read()
   text.close()
   return render_template('homepage.html', content=content, **templateData)

@app.route("/activateScripts/", methods=['GET', 'POST'])
def activateScripts():
   subprocess.call(['./scripts/activatescripts.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/checkPreRequirements/", methods=['GET', 'POST'])
def checkPreRequirements():
   subprocess.call(['./scripts/check-pre-requirements.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

# generate CSVs
# @app.route("/csv_from_excel/", methods=['GET', 'POST'])
# def csv_from_excel():
#    subprocess.Popen(['./scripts/csv_from_excel.py'], shell=True)
#    return redirect('http://127.0.0.1:5000/')

# set ENV VAR
@app.route("/set_env_var/", methods=['GET', 'POST'])
def set_env_var():
   subprocess.Popen(['./scripts/set_env_var.py'], shell=True)
   return redirect('http://127.0.0.1:5000/config')

# set ENV VAR with all quieries
@app.route("/set_env_var_all_queries/", methods=['GET', 'POST'])
def set_env_var_all_queries():
   subprocess.Popen(['./scripts/set_env_var_all_queries.py'], shell=True)
   return redirect('http://127.0.0.1:5000/config')

# choose which queries to run
@app.route("/query1/", methods=['GET', 'POST'])
def query1():
   subprocess.Popen(['/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/queries/query1.py'], shell=True)
   return redirect('http://127.0.0.1:5000/config')

# Setup the infrastructure
@app.route("/setup_the_environment/", methods=['GET', 'POST'])
def setup_the_environment():
   subprocess.call(['./scripts/setup_the_environment.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/deploy_a_bench_infrastructure/", methods=['GET', 'POST'])
def deploy_a_bench_infrastructure():
  subprocess.call(['gnome-terminal -- ./future-app/a-bench/admin.sh senv_a'], shell=True)
  # subprocess.call(['./scripts/deploy_a_bench_infrastructure.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

@app.route("/minikubeDashboard/", methods=['GET', 'POST'])
def minikubeDashboard():
  subprocess.call(['./scripts/minikubeDashboard.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

# Run
@app.route("/config/", methods=['GET', 'POST'])
def config():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M %d-%m-%Y")
   templateData = {
      'title' : 'A-Bench',
      'time': timeString
      }
   # value = request.form.getlist('check')
   return render_template('config.html', **templateData)

@app.route("/run_a_sample_experiment/", methods=['GET', 'POST'])
def run_a_sample_experiment():
  # subprocess.call(['gnome-terminal -- ./testing_foo/foo.sh'], shell=True)
  # subprocess.call(['gnome-terminal', '-x', './testing_foo/foo.sh'], shell=True)
  subprocess.call(['./scripts/run_a_sample_experiment.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

# Analyse
@app.route("/prepare_results/", methods=['GET', 'POST'])
def prepare_results():
  subprocess.call(['./scripts/prepare_results.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

@app.route('/cpuChart')
def cpuChart():
    bar_labels=cpu_labels
    bar_values=cpu_values
    return render_template('CPU_Density_Plot.html', title='CPU Usage', max=2095640174197, labels=bar_labels, values=bar_values)

@app.route('/memChart')
def memChart():
    bar_labels=mem_labels
    bar_values=mem_values
    return render_template('Mem_Density_Plot.html', title='RAM Usage', max=2095640174197, labels=bar_labels, values=bar_values)

@app.route('/fileChart')
def fileChart():
    bar_labels=file_labels
    bar_values=file_values
    return render_template('File_Density_Plot.html', title='Filesystem Usage', max=2095640174197, labels=bar_labels, values=bar_values)

if __name__ == "__main__":
   app.run(port=5000, debug=True, use_reloader=False)
