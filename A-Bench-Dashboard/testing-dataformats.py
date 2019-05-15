import pandas as pd
import json
import csv


# df = pd.read_csv("/home/vr/BigBench2-easy-deploy/experi/cpu_usage.txt", error_bad_lines=False)
# df = pd.read_csv("/home/vr/BigBench2-easy-deploy/experi/cpu_usage.txt", sep='\t', header=None, engine='python')
columns_name = ['time', 'value']
df = pd.read_fwf("/home/vr/BigBench2-easy-deploy/experi/cpu_usage.txt", header=0, usecols=columns_name, engine='python')
# df = pd.read_csv("/home/vr/Downloads/d3-flask-blog-post-master/data.csv", error_bad_lines=False, engine='python')
chart_data = df.to_dict(orient='records')
chart_data = json.dumps(chart_data, indent=2)


chart_data = json.dumps(chart_data)
data = {'chart_data': chart_data}
print(data)
# print(chart_data)
# print(df)
