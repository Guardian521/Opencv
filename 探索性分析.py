import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv
matplotlib.use('TkAgg')

data = []
with open('features_with_clusters.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        file_name = row[0]
        row = [0 if value == '' else float(value) for value in row[1:]]
        data.append([file_name] + row)
df = pd.DataFrame(data)
df.set_index(0, inplace=True)


print(df.head())

print(df.info())

print(df.describe())

# 直方图
df.hist(bins=20, figsize=(15, 10))
plt.show(block=True)

# 箱线图
df.boxplot(figsize=(15, 5))
plt.show(block=True)

df1 = pd.read_csv('features_with_clusters.csv', skiprows=0)
df2 = pd.read_excel('data_sample_400.xlsx', skiprows=0)
a = 0
for i in range(len(df1.iloc[:, 0])):
    if df1.iloc[i, 1] == df2.iloc[i, 1]:
        a += 1
accuracy = a / 400
print('Accuracy:',accuracy)