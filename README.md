# Implementig A-Bench

This is my master thesis project. The main goal is to make installing, setting up and implementing the Benchmark A-Bench easier and to automate the process as much as possible.
Using html, python3.6, flask, pandas and some other tools I created a WebUI for easier control over the setup of the infrastructure, running the benchmark and visualizing the results in a few charts which gives information about some metrics like CPU, memory and file system usage.

# Getting started
## Requirements:
*  Iternet connection
*  Ubuntu 18.04 LTS (clean install)
*  Modern web browser like Google Chrome, Mozilla Firefox, Microsoft Edge
## Tech
A-bench-dashboard uses a number of open source projects to work properly:
* [python3.6] - Python Programming Language version 3.6
* [Flask] - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [pandas] - pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language
* [chart.js] - Simple yet flexible JavaScript charting for designers & developers

**1. Step:**
* Download the repository
* Run install-pre-requirements.sh in folder scripts to install missing tools if any
* Run check-pre-requirements.sh in folder scripts to check if all the needed tools are properly installed
* To start the main WebUI run the python script in terminal:
```sh
$ sudo python start-dashboard.py
```
* Verify the deployment by navigating to your server address in your preferred browser.
```sh
127.0.0.1:5000
```
**2. Step:**
* The homepage shows three columns of buttons and text box with the output from running different commands inside the page
* First set of buttons under the "Setup" are used to  make all scripts executable, check pre-requirements, setup the environment and deploy A-Bench infrastructure
* Second set of buttons under "Run" are used to configure which quieries to be run and to run a sample A-Bench experiment
* Third set of buttons under "Analyze" are used to prepare the results after running a sample experiment and to analyze them
**3. Step:**
* After successfully running an experiment an experiment#01.zip will be saved
* Once this is done, click on the button "prepare results" so that all charts can be filled with data

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen.)

   [python3.6]: <https://github.com/python>
   [Flask]: <https://github.com/pallets/flask>
   [chart.js]: <https://github.com/chartjs/Chart.js>
   [pandas]: <https://github.com/pandas-dev/pandas>
