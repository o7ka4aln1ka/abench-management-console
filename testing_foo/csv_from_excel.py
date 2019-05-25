#!/usr/bin/env python3


import pandas as pd

# extract data from excel sheet CPU Usage and convert it to csv
data_xls = pd.read_excel('/home/vr/BigBench2-easy-deploy/exp00.xlsx', 'cpu_usage', usecols = "A,I,K")
data_xls.to_csv('/home/vr/BigBench2-easy-deploy/cpu_usage_A_I_K.csv', encoding='utf-8')

# extract data from excel sheet Memory Usage and convert it to csv
data_xls = pd.read_excel('/home/vr/BigBench2-easy-deploy/exp00.xlsx', 'memory_usage', usecols = "A,I,K")
data_xls.to_csv('/home/vr/BigBench2-easy-deploy/memory_usage_A_I_K.csv', encoding='utf-8')

# extract data from excel sheet Filesystem Usage and convert it to csv
data_xls = pd.read_excel('/home/vr/BigBench2-easy-deploy/exp00.xlsx', 'filesystem_usage', usecols = "A,J,L")
data_xls.to_csv('/home/vr/BigBench2-easy-deploy/filesystem_usage_A_J_L.csv', encoding='utf-8')

# df = pd.read_csv('/home/vr/BigBench2-easy-deploy/cpu_usage_A_B_I_K.csv', usecols=['time','value'])
# # print(df)
#
# colnames=['time', 'value']
# data = pd.read_csv('/home/vr/BigBench2-easy-deploy/cpu_usage_A_B_I_K.csv', skiprows=[0], names=colnames)
# times = data.time.tolist()
# values = data.value.tolist()
# print(times)
# print(values)
