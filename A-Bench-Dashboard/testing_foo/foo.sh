#!/bin/sh

{
echo hello && echo test if it continues && apt-get update && apt-get upgrade -y;} >> test_output.txt
# gnome-terminal -- '/bin/bash -c "cd ~/future-app/a-bench/; ./admin.sh senv_a" '
# gnome-terminal -- '(cd ~/future-app/a-bench/ && ./admin.sh senv_a)'
