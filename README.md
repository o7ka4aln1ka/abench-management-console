**Implementig A-Bench**

This is my master thesis project. The main goal is to make installing and implementing the Benchmark A-Bench easier and to automate the process as much as possible.

Using html, python3.6, flask, pandas and some other tools I created a WebUI for easier control over the setup of the infrastructure, running the benchmark and

visualizing the results in a few charts which gives information about some metrics like CPU, memory and file system usage.

**Pre-requirements:**

*  Ubuntu 18.04 LTS (clean install)
*  python 3.6.x
*  flask - latest version
*  pandas - latest version

**1. Step:**

* Make sure that all the pre-required software is installed
* Download the repository
* Run the python script in terminal: python start-dashboard.py
* Go to a browser and open: 127.0.0.1:5000

**2. Step:**

* The homepage shows three columns of buttons
* First set of buttons under the "Setup" are used to prepare the infrastructure and install all the necessary software
* Second set of buttons under "Run" are used to start the A-Bench
* Third set of buttons under "Analyze" are used to analyze the results after running A-Bench
