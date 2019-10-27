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
import shutil
from tkinter import *
from tkinter import filedialog

def prepare_results():
    file = request.files['myFile']
    subprocess.call(["mkdir", "tmp"])
    filePath = os.path.join("./tmp", file.filename)
    file.save(filePath)
    subprocess.call(['chmod', '777', '.', filePath])
    with zipfile.ZipFile(filePath, 'r') as zf:
       for file in zf.namelist():
            if file.endswith("cpu_usage.txt") or file.endswith("memory_usage.txt") or file.endswith("filesystem_usage.txt"):
                zf.extract(file, basepath + "/experiment_results")
    zf.close()
    os.chmod(basepath + "/experiment_results", 0o777)
    shutil.rmtree("./tmp")
    print("Successfully loaded experiment data!")

    prepare_results()
