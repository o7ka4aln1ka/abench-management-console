#!/bin/sh

(gnome-terminal -- find ~/github/a-bench-dashboard/scripts -type f -iname "*.sh" -exec chmod +x {} &&\
echo All .sh scripts were made executable\ &&
gnome-terminal -- find ~/github/a-bench-dashboard/scripts -type f -iname "*.py" -exec chmod +x {} &&\
echo TEST &&\
echo All .py scripts were made executable\
) 2>&1 | tee -a ~/github/a-bench-dashboard/output-homepage.txt
