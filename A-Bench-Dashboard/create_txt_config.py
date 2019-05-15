#!/usr/bin/env python3

import os
import stat

file = open("config/config.sh   ", "w+")
file.write("cd $home_container_bench && hive -f queries/")
file.close()

# give permisions to folder/files
# os.chdir('/home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/queries')
# os.system(sudo chmod -R -f 777 /home/vr/BigBench2-easy-deploy/A-Bench-Dashboard/queries/)
# os.chmod('query1.py', 777)
# os.chmod('query1.py', stat.S_IEXEC)
# os.chmod('query2.py', stat.S_IEXEC)
# os.chmod('query3.py', stat.S_IEXEC)
# os.chmod('query4.py', stat.S_IEXEC)
# os.chmod('query5.py', stat.S_IEXEC)
