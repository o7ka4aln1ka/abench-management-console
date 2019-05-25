#!/bin/sh

gnome-terminal -- find ~/BigBench2-easy-deploy/A-Bench-Dashboard/scripts -type f -iname "*.sh" -exec chmod +x {} \;
gnome-terminal -- find ~/BigBench2-easy-deploy/A-Bench-Dashboard/scripts -type f -iname "*.py" -exec chmod +x {} \;
