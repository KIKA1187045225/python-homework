'''
作者：陈其佳
班别：物理161
学号：1619100004
'''

n=[31,28,31,30,31,30,31,31,30,31,30,31]
l=[31,29,31,30,31,30,31,31,30,31,30,31]
def leap_year(y):
    days=0
    if ((y%4)==0 and (y%100)!=0)or (y%400)==0:
        days=366
    else:
        days=365
    return days

def count_date():
    if y2>y1: #不同一年的比较
        if leap_year(y1)==366:
            days1=l[m1-1]-d1
            for i in range(12-m1):
                days1=days1+l[m1+i]
        if leap_year(y1)==365:
            days1=n[m1-1]-d1
            for i in range(12-m1):
                days1=days1+n[m1+i]

        days2=0
        for i in range(1,y2-y1):
            if leap_year(i+y1)==366:
                days2=days2+366
            if leap_year(i+y1)==365:
                days2=days2+365

        if leap_year(y2)==366:
            days3=d2
            for i in range(m2-1):
                days3=l[i]+days3
        if leap_year(y2)==365:
            days3=d2
            for i in range(m2-1):
                days3=n[i]+days3

    if y2==y1: #同一年的比较
        if m2>m1: #不同月份
            if leap_year(y1)==366:
                days1=l[m1-1]-d1
                days2=0
                for i in range(m2-m1-1):
                    days2=days2+l[i+m1]
                days3=d2
            if leap_year(y1)==365:
                days1=n[m1-1]-d1
                days2=0
                for i in range(m2-m1-1):
                    days2=days2+n[i+m1]
                days3=d2
        if m2==m1: #同年同月
            days1=0
            days2=0
            days3=d2-d1
        
    return days1+days2+days3
print('''
----本程序用于计算两个日期间隔的天数----
    注意事项：
    1.日期1要比日期2早。
    2.输入法要求英文输入法，格式示例：xx,xx,xx  --->如2019,9,10
''')

while 1:
    print("")
    date_1=input("请输入日期1：")
    strlist_1=date_1.split(',')
    y1=int(strlist_1[0])
    m1=int(strlist_1[1])
    d1=int(strlist_1[2])
    if 1<=m1<=12:#判断日期1是否有效
        if leap_year(y1)==366:
            if not 1<=d1<=l[m1-1]:
                print("日期1为无效日期！")
                continue
        if leap_year(y1)==365:
            if not 1<=d1<=n[m1-1]:
                print("日期1为无效日期！")
                continue
    if not 1<=m1<=12:
        print("日期1为无效日期！")
        continue    

    date_2=input("请输入日期2：")
    strlist_2=date_2.split(',')
    y2=int(strlist_2[0])
    m2=int(strlist_2[1])
    d2=int(strlist_2[2])
    if 1<=m2<=12:#判断日期2是否有效
        if leap_year(y2)==366:
            if not 1<=d2<=l[m2-1]:
                print("日期2为无效日期！")
                continue
        if leap_year(y2)==365:
            if not 1<=d2<=n[m2-1]:
                print("日期2为无效日期！")
                continue
    if not 1<=m2<=12:
        print("日期2为无效日期！")
        continue
    
    if y2<y1:
        print("日期1晚于日期2，输入无效！")
        continue
    if y2==y1:
        if m2==m1:
            if not d2>d1:
                print("日期1晚于日期2，输入无效！")
                continue
        if m2<m1:
            print("日期1晚于日期2，输入无效！")
            continue

    m=count_date()
    print("两个日期间隔",m,"天")
    a=input("按空格键退出程序/任意键继续")
    if a==' ':
        break