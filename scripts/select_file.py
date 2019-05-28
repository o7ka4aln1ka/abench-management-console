import tkinter
from tkinter import filedialog
import os

def upload_file():
    tkinter.Tk().withdraw() # Close the root window
    in_path = filedialog.askopenfilename()
    os.environ['PATH_TO_EXPERIMENTS_ZIP'] = in_path
    print('Path to experiment#01.zip = ', os.environ['PATH_TO_EXPERIMENTS_ZIP'])
    print ('Path to the results of last experiment is ' + in_path)

if __name__== "__main__":
    upload_file()
