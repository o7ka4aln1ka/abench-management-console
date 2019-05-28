#!/bin/sh

# run a sample experiment
(
cd ~/github/a-bench-dashboard/submodules/a-bench/future-app/a-bench/ &&
./admin.sh run_sample_sre_bbv
) 2>&1 | tee -a ~/github/a-bench-dashboard/outputs/output-homepage.txt
