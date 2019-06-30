1. [ Implementig A-Bench ](#implementing)
  - [ Requirements ](#req)
  - [ Tech ](#tech)
2. [ Getting started ](#get)
  - [ 1. Step ](#1st)
  - [ 2. Step ](#2nd)
  - [ 3. Step ](#3rd)
  - [ 4. Step ](#4th)
3. [ Additional information ](#add)

<a name="implementing"></a>
# Implementig A-Bench

This is my master thesis project. The main goal is to make installing, setting up and implementing the Big Data Benchmark A-Bench easier and to automate the process as much as possible.
Using html, python3.6, flask, pandas and some other tools I created a WebUI management console for easier control over the setup of the infrastructure, running the benchmark and visualizing the results in a few charts which gives information about some metrics like CPU, memory and file system usage.

<a name="req"></a>
## Requirements:
*  Iternet connection
*  Ubuntu 18.04 LTS (clean install)
*  Modern web browser like Chromium or Mozilla Firefox
<a name="tech"></a>
## Tech
The ABench management console uses a number of open source projects to work properly:
* [python3.6] - Python Programming Language version 3.6
* [Flask] - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [pandas] - pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language
* [chart.js] - Simple yet flexible JavaScript charting for designers & developers

<a name="get"></a>
# Getting started
<a name="1st"></a>
**1. Step:**
* Download the repository into home/user/github/ in order to work properly
* Go go project folder "scripts" and run install_requirements.sh as root to install missing tools if any and download a GitHub repository for creating [A-Bench infrastructure]
```sh
$ sudo install_requirements.sh
```
* To start the main WebUI run the python script in terminal as root:
```sh
$ sudo python abench-management-console.py
```
* Verify the deployment by navigating to your server address in your preferred browser
```sh
http://127.0.0.1:5000
```
<a name="2nd"></a>
**2. Step:**
* On the homepage there are three columns of buttons to the left and text box with the output from running different commands inside the page to the right
* First set of buttons under the "Setup" are used to check pre-requirements, if everything needed is installed, setup the environment using [A-Bench infrastructure] and to deploy [A-Bench infrastructure]
* Second set of buttons under "Run" are used to configure which queries to be run and to run a sample ABench experiment after going to "Configuration" page and selecting the queries
* Third set of buttons under "Analyze" are used to load the results ONLY AFTER running a sample experiment described in 3.Step.

<a name="3rd"></a>
**3. Step:**
* When you click the button "Configuration" under "Run" you will be forwarded to a new page
* There are shown all 30 queries with explanation that can be run as an experiment as a check boxes
* After selecting the desired one click "Save config" and under the field with all queries the chosen one will be shown
* A environment variable will be created and after clicking "Run a sample experiment" this variable would be used

<a name="4th"></a>
**4. Step:**
* After successfully running an experiment the results will be saved in:
```sh
/submodules/a-bench/results/
```
* On the homepage under "Analyze" by clicking on "Load results" a file explorer will open, navigate to ~/github/abench-management-console/submodules/a-bench/results, choose the experiment_tag_sample_qXX.zip file name to load the results and analyze them using charts
* If you want to load new results from different experiment repeat the previous step

<a name="add"></a>
# Additional Information
* In the folder "experiment_results" will be saved as a .csv tables the results from the experiment needed for the charts
* In the folder "outputs" are two .txt files used for the output from all executed commands to be shown on the homepage
* In the folder "scripts" are all necessary scripts for deploying and running the infrastructure
* In the folder "templates" are all html pages
* In the folder "static" are located all .css files for the styling of the pages
* In folder "submodules" will be downloaded everything necessary for the infrastructure from GitHub repository https://github.com/FutureApp/a-bench from Michael Czaja

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen.)

   [python3.6]: <https://github.com/python>
   [Flask]: <https://github.com/pallets/flask>
   [chart.js]: <https://github.com/chartjs/Chart.js>
   [pandas]: <https://github.com/pandas-dev/pandas>
   [A-Bench infrastructure]: <https://github.com/FutureApp/a-bench>
