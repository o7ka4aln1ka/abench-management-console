#!/bin/sh
# sudo find . -name 'experiment#01.zip*' &&
cd /home/vr/BigBench2-easy-deploy/future-app/a-bench/results && sudo chmod -R 777 .
sleep 5
cd "$(dirname "$(find . -name 'experiment#01.zip*')")"
sleep 5
# chmod 777 'experiment#01.zip'
mkdir experiment_results
unzip 'experiment#01.zip' -d experiment_results
