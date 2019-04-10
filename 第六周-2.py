'''
    作者：陈其佳
    班别：物理161
    学号：1619100004
    功能:创建excel表格，并写进一些内容
'''
#方法1

# import pandas as pd

# Name=['Mayi','Jack','Tom','Rain','Hanmeimei']
# Age=[18,21,25,19,23]
# Score=[99,89,95,80,81]
# No=[1,2,3,4,5]
# a=[Name,Age,Score]

# dataframe=pd.DataFrame({'No.':No,'Name':a[0],'Age':a[1],'Score':a[2]})
# dataframe.to_csv(r"D:\Week sixth.csv",index=False,sep=',')

#方法2

import csv

Name=['Mayi','Jack','Tom','Rain','Hanmeimei']
Age=[18,21,25,19,23]
Score=[99,89,95,80,81]
a=[Name,Age,Score]

with open(r'D:\Week sixth.csv','w',newline="") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['No.','Name','Age','Score'])
    for i in range(5):
        writer.writerow([i+1,a[0][i],a[1][i],a[2][i]])