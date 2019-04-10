'''
作者：陈其佳
班别：物理161
学号：1619100004
功能：读CSV文件：aapl.csv,给出全部数据中Volume的平均值。
'''
import csv

Volume=[]
with open("aapl.csv",'r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        Volume.append(row[5])

sum=0
for i in range(1,len(Volume)):
    sum=sum+int(Volume[i])
ave=sum/(len(Volume)-1)
print(Volume[0],"的平均值为:",ave)