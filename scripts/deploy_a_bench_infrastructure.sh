#!/bin/sh

cd ~/github/a-bench-dashboard/submodules/a-bench/ >> ~/github/a-bench-dashboard/test_output.txt
sudo ./admin.sh senv_a >> ~/github/a-bench-dashboard/test_output.txt
sudo ./admin.sh down_submodules >> ~/github/a-bench-dashboard/test_output.txt
