#!/bin/sh
# sudo find . -name 'experiment#01.zip*' &&
cd /home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/future-app/a-bench/results && sudo chmod -R 777 .
sleep 5
cd "$(dirname "$(find . -name 'experiment#01.zip*')")"
sleep 5
mkdir experiment_results
unzip 'experiment#01.zip' -d experiment_results
chmod -R 777 experiment_results
