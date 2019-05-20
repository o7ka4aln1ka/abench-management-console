#!/bin/sh

echo hello
gnome-terminal -- '/bin/bash -c "cd ~/future-app/a-bench/; ./admin.sh senv_a" '
gnome-terminal -- '(cd ~/future-app/a-bench/ && ./admin.sh senv_a)'
