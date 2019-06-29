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
      'time': timeString
      }
#  Loads an output file to be shown in text box on homepage
   text = open(basepath + '/outputs/output-homepage.txt', 'r+')
   content = text.read()
   text.close()
   return render_template('homepage.html', content=content, **templateData)

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
  # subprocess.call('./future-app/a-bench/admin.sh senv_a', shell=True)
  subprocess.call(['./scripts/deploy_a_bench_infrastructure.sh'], shell=True)
  return redirect('http://127.0.0.1:5000/')

# 2nd column of buttons "Run"
@app.route("/config/", methods=['GET', 'POST'])
def config():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M %d-%m-%Y")
   templateData = {
      'time': timeString
      }
   # value = request.form.getlist('check')
   return render_template('config.html', **templateData)

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
   queriesOptions = {'q1': "Unchecked", 'q2': "Unchecked", 'q3': "Unchecked", 'q4': "Unchecked", 'q5': "Unchecked",\
                   'q6': "Unchecked", 'q7': "Unchecked", 'q8': "Unchecked", 'q9': "Unchecked", 'q10': "Unchecked",\
                   'q11': "Unchecked", 'q12': "Unchecked", 'q13': "Unchecked", 'q14': "Unchecked", 'q15': "Unchecked",\
                   'q16': "Unchecked", 'q17': "Unchecked", 'q18': "Unchecked", 'q19': "Unchecked", 'q20': "Unchecked",\
                   'q21': "Unchecked", 'q22': "Unchecked", 'q23': "Unchecked", 'q24': "Unchecked", 'q25': "Unchecked",\
                   'q26': "Unchecked", 'q27': "Unchecked", 'q28': "Unchecked", 'q29': "Unchecked", 'q30': "Unchecked"}
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
   print("The following queries will be executed: " + varQueries)
   print('TEST_QUERIES = ', os.environ['TEST_QUERIES'])
   # returns a test page to see which queries are chosen
   # return render_template("test.html", test_name=queriesOptions)
   return render_template("config.html", content=content, test_name=queriesOptions, **templateData)

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
    testPath = "~/github/abench-management-console/experiment_results/"
    cpu_data = pd.read_fwf(testPath + "cpu_usage.txt", header=0, usecols=cpu_colnames, engine='python')
    cpu_labels = cpu_data.time.tolist()
    cpu_values = cpu_data.value.tolist()
    now = datetime.datetime.now()
    timeString = now.strftime("%H:%M %d-%m-%Y")
    bar_labels=cpu_labels
    bar_values=cpu_values

    # CPU Load in percentage
    maxCPUValue = max(cpu_values)
    new_bar=[(x / maxCPUValue)*100 for x in bar_values]

    # calculate the duration
    date_time_str_start = bar_labels[0]
    date_time_obj_start = datetime.datetime.strptime(date_time_str_start, '%Y-%m-%dT%H:%M:%SZ')
    date_time_str_end = bar_labels[-1]
    date_time_obj_end = datetime.datetime.strptime(date_time_str_end, '%Y-%m-%dT%H:%M:%SZ')
    cpu_duration = date_time_obj_end - date_time_obj_start
    max_value = max(cpu_values) + 1000
    print(max(cpu_values))
    templateData = {
        'time': timeString,
        'duration': cpu_duration
    }
    return render_template('CPU_Density_Plot.html', title='CPU Usage', max=max_value, labels=bar_labels, values=new_bar, **templateData)

@app.route('/memChart')
def memChart():
    mem_colnames=['time', 'value']
    mem_data = pd.read_fwf("~/github/abench-management-console/experiment_results/memory_usage.txt", header=0, usecols=mem_colnames, engine='python')
    mem_labels = mem_data.time.tolist()
    mem_values = mem_data.value.tolist()
    now = datetime.datetime.now()
    timeString = now.strftime("%H:%M %d-%m-%Y")

    bar_labels=mem_labels
    bar_values=mem_values

    # Memory Load in percentage
    maxMemValue = max(mem_values)
    new_bar=[(x / maxMemValue)*100 for x in bar_values]

    # calculate the duration
    date_time_str_start = bar_labels[0]
    date_time_obj_start = datetime.datetime.strptime(date_time_str_start, '%Y-%m-%dT%H:%M:%SZ')
    date_time_str_end = bar_labels[-1]
    date_time_obj_end = datetime.datetime.strptime(date_time_str_end, '%Y-%m-%dT%H:%M:%SZ')
    mem_duration = date_time_obj_end - date_time_obj_start
    # print("Memory Duration: ", mem_duration)
    max_value = max(mem_values) + 1000
    templateData = {
        'time': timeString,
        'duration': mem_duration
    }
    return render_template('Mem_Density_Plot.html', title='RAM Usage', max=max_value, labels=bar_labels, values=new_bar, **templateData)

@app.route('/fileChart')
def fileChart():
    file_colnames=['time', 'value']
    file_data = pd.read_fwf("~/github/abench-management-console/experiment_results/filesystem_usage.txt", header=0, usecols=file_colnames, engine='python')
    file_labels = file_data.time.tolist()
    file_values = file_data.value.tolist()
    now = datetime.datetime.now()
    timeString = now.strftime("%H:%M %d-%m-%Y")

    bar_labels=file_labels
    bar_values=file_values

    # Filesystem Load in percentage
    maxFileValue = max(file_values)
    new_bar=[(x / maxFileValue)*100 for x in bar_values]

    # calculate the duration
    date_time_str_start = bar_labels[0]
    date_time_obj_start = datetime.datetime.strptime(date_time_str_start, '%Y-%m-%dT%H:%M:%SZ')
    date_time_str_end = bar_labels[-1]
    date_time_obj_end = datetime.datetime.strptime(date_time_str_end, '%Y-%m-%dT%H:%M:%SZ')
    file_duration = date_time_obj_end - date_time_obj_start
    # print("Filesystem Duration: ", file_duration)
    max_value = max(file_values) + 1000
    templateData = {
        'time': timeString,
        'duration': file_duration
    }
    return render_template('File_Density_Plot.html', title='Filesystem Usage', max=max_value, labels=bar_labels, values=new_bar, **templateData)

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
    # zip_ref.extractall("/home/vr/github/abench-management-console/experiment_results")
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

# -------------------------------------
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
# @app.route('/prepare_results/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return redirect('http://127.0.0.1:5000/')


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
