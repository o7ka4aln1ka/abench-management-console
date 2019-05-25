#!/bin/sh

(cd ~/github/a-bench-dashboard/scripts -type f -iname "*.sh" -exec chmod +x {}
echo All .sh scripts were made executable
cd ~/github/a-bench-dashboard/scripts -type f -iname "*.py" -exec chmod +x {}
echo All .py scripts were made executable
pwd
) 2>&1 | tee -a ~/github/a-bench-dashboard/output-homepage.txt
