#!/bin/sh

cd ~/github/a-bench-dashboard/submodules/a-bench/future-app/a-bench/
./admin.sh run_sample_sre_bbv 2>&1 | tee -a ~/github/a-bench-dashboard/test_output.txt
