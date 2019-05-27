# main script for starting the webui

from flask import Flask, render_template, redirect, request, jsonify, make_response, send_from_directory
import subprocess
from subprocess import Popen, PIPE
import os
import datetime
import time
import pandas as pd
import json
import csv

app = Flask(__name__)

basepath = os.path.abspath(".")

#  homepage
@app.route("/", methods=['GET', 'POST'])
def home():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M %d-%m-%Y")
   templateData = {
      'title' : 'A-Bench',
      'time': timeString
      }
#  Loads an output file to be shown in text box on homepage
   text = open(basepath + '/output-homepage.txt', 'r+')
   content = text.read()
   text.close()
   return render_template('homepage-v2.html', content=content, **templateData)

#  @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon)

# 1st column of buttons "Setup"
@app.route("/installRequirements/", methods=['GET', 'POST'])
def installRequirements():
   subprocess.call(['./scripts/install_requirements.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/activateScripts/", methods=['GET', 'POST'])
def activateScripts():
   subprocess.call(['./scripts/activate_scripts.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/checkPreRequirements/", methods=['GET', 'POST'])
def checkPreRequirements():
   subprocess.call(['./scripts/check_pre_requirements.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

# Setup the infrastructure
@app.route("/setupEnvironment/", methods=['GET', 'POST'])
def setupEnvironment():
   subprocess.call(['./scripts/setup_environment.sh'], shell=True)
   return redirect('http://127.0.0.1:5000/')

@app.route("/deploy_a_bench_infrastructure/", methods=['GET', 'POST'])
def deploy_a_bench_infrastructure():
  subprocess.call('sudo ./future-app/a-bench/admin.sh senv_a', shell=True)
  # subprocess.call(['./scripts/deploy_a_bench_infrastructure.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

# 2nd column of buttons "Run"
@app.route("/config/", methods=['GET', 'POST'])
def config():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M %d-%m-%Y")
   templateData = {
      'title' : 'A-Bench',
      'time': timeString
      }
   # value = request.form.getlist('check')
   return render_template('config-v2.html', **templateData)

# config.html
# choose which queries to run
@app.route("/set_env_var/", methods=['POST'])
def set_env_var():
   queriesList = []
   # setuo all checkboxes to Unchecked
   queriesOptions = {'1': "Unchecked", '2': "Unchecked", '3': "Unchecked", '4': "Unchecked", '5': "Unchecked",\
                   '6': "Unchecked", '7': "Unchecked", '8': "Unchecked", '9': "Unchecked", '10': "Unchecked",\
                   '11': "Unchecked", '12': "Unchecked", '13': "Unchecked", '14': "Unchecked", '15': "Unchecked",\
                   '16': "Unchecked", '17': "Unchecked", '18': "Unchecked", '19': "Unchecked", '20': "Unchecked",\
                   '21': "Unchecked", '22': "Unchecked", '23': "Unchecked", '24': "Unchecked", '25': "Unchecked",\
                   '26': "Unchecked", '27': "Unchecked", '28': "Unchecked", '29': "Unchecked", '30': "Unchecked"}
   for key in queriesOptions.keys():
       # change to Checked if a query is selected
       if request.form.get(key):
           queriesOptions[key] = "Checked"
           varQueries = ""
           for key,value in queriesOptions.items():
               if value == "Checked":
                   varQueries = varQueries + key + " "
                   # set ENV VAR
                   os.environ['TEST_QUERIES'] = varQueries
   # returns a test page to see which queries are chosen
   return render_template("test.html", test_name=queriesOptions)

# set ENV VAR with all quieries
@app.route("/set_env_var_all_queries/", methods=['GET', 'POST'])
def set_env_var_all_queries():
   subprocess.Popen(['./scripts/set_env_var_all_queries.py'], shell=True)
   return redirect('http://127.0.0.1:5000/config')

@app.route("/run_a_sample_experiment/", methods=['GET', 'POST'])
def run_a_sample_experiment():
  subprocess.call(['./scripts/run_a_sample_experiment.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')


# 3rd column of buttons "Analyse"
# unzips experiment#01.zip after running a sample experiment
@app.route("/prepare_results/", methods=['GET', 'POST'])
def prepare_results():
  subprocess.call(['./scripts/prepare_results.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

# loading the data for the charts after running the experiments
cpu_colnames=['time', 'value']
cpu_data = pd.read_fwf("~/github/a-bench-dashboard/experiment_results/cpu_usage.txt", header=0, usecols=cpu_colnames, engine='python')
cpu_labels = cpu_data.time.tolist()
cpu_values = cpu_data.value.tolist()

mem_colnames=['time', 'value']
mem_data = pd.read_fwf("~/github/a-bench-dashboard/experiment_results/memory_usage.txt", header=0, usecols=mem_colnames, engine='python')
mem_labels = mem_data.time.tolist()
mem_values = mem_data.value.tolist()

file_colnames=['time', 'value']
file_data = pd.read_fwf("~/github/a-bench-dashboard/experiment_results/filesystem_usage.txt", header=0, usecols=file_colnames, engine='python')
file_labels = file_data.time.tolist()
file_values = file_data.value.tolist()

# CPU, Memory and Filesystem charts
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

# #######################################################################
# testing foo
@app.route("/foo/", methods=['GET', 'POST'])
def foo():
    subprocess.call(['./testing_foo/foo.sh'], shell=True)
    return redirect('http://127.0.0.1:5000/')
# #######################################################################


#  start the app with debugging enabled
if __name__ == "__main__":
   app.run(port=5000, debug=True, use_reloader=False)
