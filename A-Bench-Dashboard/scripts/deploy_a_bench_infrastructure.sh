#!/bin/sh

cd /home/vr/BigBench2-easy-deploy/future-app/a-bench/ >> test_output.txt
sudo ./admin.sh senv_a >> test_output.txt
sudo ./admin.sh down_submodules >> test_output.txt
