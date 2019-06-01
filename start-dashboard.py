from flask import Flask, render_template, redirect, request, jsonify, make_response, send_from_directory
import subprocess
from subprocess import Popen, PIPE
from werkzeug import secure_filename
import os
import datetime
import time
import pandas as pd
import json
import csv
import zipfile
import tkinter
from tkinter import filedialog

# set path to upload experiment#01.zip
UPLOAD_FOLDER = './experiment_results'

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
   text = open(basepath + '/outputs/output-homepage.txt', 'r+')
   content = text.read()
   text.close()
   return render_template('homepage-v2.html', content=content, **templateData)

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
  subprocess.call('./future-app/a-bench/admin.sh senv_a', shell=True)
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
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M %d-%m-%Y")
   templateData = {
       'time': timeString
   }
   queriesList = []
   # setups all checkboxes to Unchecked
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
                   with open('outputs/selectedQueries.txt', 'w') as fo:
                       fo.write(varQueries)
   #  Loads an output file to be shown in text box on homepage
   text = open(basepath + '/outputs/selectedQueries.txt', 'r+')
   content = text.read()
   text.close()
   # returns a test page to see which queries are chosen
   # return render_template("test.html", test_name=queriesOptions)
   return render_template("config-v2.html", content=content, test_name=queriesOptions, **templateData)

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
# @app.route("/prepare_results/", methods=['GET', 'POST'])
# def prepare_results():
#   subprocess.call(['./scripts/prepare_results.sh'], shell=True)
#   return redirect('http://127.0.0.1:5000/')

# CPU, Memory and Filesystem charts
@app.route('/cpuChart')
def cpuChart():
    cpu_colnames=['time', 'value']
    testPath = "~/github/a-bench-dashboard/experiment_results/"
    cpu_data = pd.read_fwf(testPath + "cpu_usage.txt", header=0, usecols=cpu_colnames, engine='python')
    cpu_labels = cpu_data.time.tolist()
    cpu_values = cpu_data.value.tolist()
    now = datetime.datetime.now()
    timeString = now.strftime("%H:%M %d-%m-%Y")
    templateData = {
       'time': timeString
       }
    bar_labels=cpu_labels
    bar_values=cpu_values
    return render_template('CPU_Density_Plot-v3.html', title='CPU Usage', max=2095640174197, labels=bar_labels, values=bar_values, **templateData)

@app.route('/memChart')
def memChart():
    mem_colnames=['time', 'value']
    mem_data = pd.read_fwf("~/github/a-bench-dashboard/experiment_results/memory_usage.txt", header=0, usecols=mem_colnames, engine='python')
    mem_labels = mem_data.time.tolist()
    mem_values = mem_data.value.tolist()
    now = datetime.datetime.now()
    timeString = now.strftime("%H:%M %d-%m-%Y")
    templateData = {
        'time': timeString
       }
    bar_labels=mem_labels
    bar_values=mem_values
    return render_template('Mem_Density_Plot-v3.html', title='RAM Usage', max=2095640174197, labels=bar_labels, values=bar_values, **templateData)

@app.route('/fileChart')
def fileChart():
    file_colnames=['time', 'value']
    file_data = pd.read_fwf("~/github/a-bench-dashboard/experiment_results/filesystem_usage.txt", header=0, usecols=file_colnames, engine='python')
    file_labels = file_data.time.tolist()
    file_values = file_data.value.tolist()
    now = datetime.datetime.now()
    timeString = now.strftime("%H:%M %d-%m-%Y")
    templateData = {
       'time': timeString
       }
    bar_labels=file_labels
    bar_values=file_values
    return render_template('File_Density_Plot-v3.html', title='Filesystem Usage', max=2095640174197, labels=bar_labels, values=bar_values, **templateData)

# #######################################################################
# testing foo
@app.route("/foo/", methods=['GET', 'POST'])
def foo():
    # subprocess.call(['./testing_foo/foo.sh'], shell=True)
    return redirect('http://127.0.0.1:5000/upload')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# save experiment#01.zip path to a variable
@app.route("/prepare_results/", methods=['GET', 'POST'])
def prepare_results():
# @app.route('/upload')
# def upload_file():
    check = False
    tkinter.Tk().withdraw() # Close the root window
    in_path = filedialog.askopenfilename()
    # os.environ['PATH_TO_EXPERIMENTS_ZIP'] = in_path
    # os.chdir(in_path)
    # zip_ref = zipfile.ZipFile(in_path, 'r')
    # zip_ref.extractall("/home/vr/github/a-bench-dashboard/experiment_results")
    # zip_ref.close()
    subprocess.call(['chmod', '-R', '777', in_path])
    with zipfile.ZipFile(in_path, 'r') as zf:
       for file in zf.namelist():
            if file.endswith("cpu_usage.txt") or file.endswith("memory_usage.txt") or file.endswith("filesystem_usage.txt"):
                zf.extract(file, basepath + "/experiment_results")
    zf.close()
    os.chmod(basepath + "/experiment_results", 0o777)
    check = True
    if check == True:
        print("Successfully loaded experiment data!")
    else:
        print("Something went wrong. Try again!")
    # print('Path to experiment#01.zip = ', os.environ['PATH_TO_EXPERIMENTS_ZIP'])
    # print ('Path to the results of last experiment is ' + in_path)
    # return render_template('test.html')
    return redirect('http://127.0.0.1:5000/')

# find experiment#01.zip and upload it to directory experiment_results
# @app.route('/uploader', methods = ['GET', 'POST'])
# def uploaded_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       filename = secure_filename(f.filename)
#       f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#       return 'file uploaded successfully'

# #######################################################################


#  start the app with debugging enabled
if __name__ == "__main__":
   app.run(port=5000, debug=True, use_reloader=False)
