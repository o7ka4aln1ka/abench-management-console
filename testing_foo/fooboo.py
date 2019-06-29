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

basepath = os.path("./github/abench-management-console/submodules/a-bench/results/")
# basepath = os.path.abspath(".")
print(basepath)

# @app.route("/prepare_results/", methods=['GET', 'POST'])
# def prepare_results():
# @app.route('/upload')
# def upload_file():
    # check = False
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
# check = True
# if check == True:
print("Successfully loaded experiment data!")
    # else:
    #     print("Something went wrong. Try again!")
    # print('Path to experiment#01.zip = ', os.environ['PATH_TO_EXPERIMENTS_ZIP'])
    # print ('Path to the results of last experiment is ' + in_path)
    # return render_template('test.html')
    # return redirect('http://127.0.0.1:5000/')

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
