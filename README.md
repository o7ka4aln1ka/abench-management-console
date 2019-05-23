**Implementig A-Bench**

This is my master thesis project. The main goal is to make installing, setting up and implementing the Benchmark A-Bench easier and to automate the process as much as possible.

Using html, python3.6, flask, pandas and some other tools I created a WebUI for easier control over the setup of the infrastructure, running the benchmark and

visualizing the results in a few charts which gives information about some metrics like CPU, memory and file system usage.

**Pre-requirements:**

*  Internet connection
*  Ubuntu 18.04 LTS (clean install)
*  Modern web browser like Google Chrome, Mozilla Firefox, Microsoft Edge
*  python 3.6.x
*  flask - latest version
*  pandas - latest version
*  chart.js - latest version

**1. Step:**

* Download the repository
* Run install-pre-requirements.sh in folder scripts to install missing tools if any
* Run check-pre-requirements.sh in folder scripts to check if all the needed tools are properly installed
* To start the main WebUI run the python script in terminal: sudo python start-dashboard.py
* Go to a browser and open: 127.0.0.1:5000

**2. Step:**

* The homepage shows three columns of buttons and text box with the output from running different commands inside the page
* First set of buttons under the "Setup" are used to  make all scripts executable, check pre-requirements, setup the environment and deploy A-Bench infrastructure
* Second set of buttons under "Run" are used to configure which quieries to be run and to run a sample A-Bench experiment
* Third set of buttons under "Analyze" are used to prepare the results after running a sample experiment and to analyze them
