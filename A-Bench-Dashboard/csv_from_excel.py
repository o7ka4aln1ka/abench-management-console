import pandas as pd

# data_xls = pd.read_excel('/home/vr/BigBench2-easy-deploy/cpu_usage_EXCEL.xlsx', 'Sheet1', usecols = "A,B,I,K")
# data_xls.to_csv('/home/vr/BigBench2-easy-deploy/cpu_usage_A_B_I_K.csv', encoding='utf-8')


df = pd.read_csv('/home/vr/BigBench2-easy-deploy/cpu_usage_A_B_I_K.csv', usecols=['time','value'])
# print(df)

colnames=['time', 'value']
data = pd.read_csv('/home/vr/BigBench2-easy-deploy/cpu_usage_A_B_I_K.csv', skiprows=[0], names=colnames)
times = data.time.tolist()
values = data.value.tolist()
# print(times)
print(values)

# MyValues = []
# MyValues.append(times)
# print(MyValues)
# values = pd.read_csv('/home/vr/BigBench2-easy-deploy/cpu_usage_A_B_I_K.csv', delimiter=',')
# for row in values:
