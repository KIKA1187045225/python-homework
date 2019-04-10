'''
    作者：陈其佳
    班别：物理161
    学号：1619100004
    功能：
        随机产生50个数字，存一个列表中 list，
        然后从小到大排序，然后写入文件，
        然后从文件中读取出来文件内容，
        然后反序，在追加到文件的下一行中。

'''


import random as r

a=[]
for i in range(50):
    n=int(r.random()*1000)
    while n in a is True:
        n=int(r.random()*1000)
    a.append(n)

a.sort()

f=open('D:\Week sixth.txt','w')
for i in range(len(a)):
    f.write(str(a[i])+' ')
    if i==24:
        f.write('\n')
f.close()
f=open('D:\Week sixth.txt','r')
print(f.read())

a.reverse()
f=open('D:\Week sixth.txt','a')
f.write('\n')
for i in range(len(a)):
    f.write(str(a[i])+' ')
    if i==24:
        f.write('\n')
f.close()
f=open('D:\Week sixth.txt','r')
print('')
print(f.read())
