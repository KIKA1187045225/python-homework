'''
作者：陈其佳
班别：物理161
学号：1619100004
'''
import random as r

def func5(dictionary):#5.查看所有联系人
    i=0
    for key,value in dictionary.items():
        i=i+1
        print(i,'.',key,":",value)

def name():#随机产生姓名
    First_Name=['陈','林','黄','郑','戚','苏','简','董','崔','袁','刘',
    '王','张','梁','甘','何','罗','蔡','杨','邓','潘']
    Last_Name=['其其','佳佳','晶晶','静静','菁菁','婧婧','琪琪','齐齐',
    '琦琦','奇奇','七七','嘉佳','加加','嘉嘉','家家','冠希','奕迅','伊凡',
    '徐坤','超越','学友','德华','紫棋','玮柏','baby','honey','darling',
    'sweetheart','Tony','Thor','热狗','思聪','雯焱','姗玲','小琪','寒桥',
    '冬夜','明建','蕊萱','紫菅']
    f_n=r.randint(0,len(First_Name)-1)
    l_n=r.randint(0,len(Last_Name)-1)
    return First_Name[f_n]+Last_Name[l_n]

def number():#随机产生手机号码
    prelist=["130","131","132","133","134",
             "135","136","137","138","139",
             "150","151","152","153","155",
             "156","157","158","186","187"]
    return r.choice(prelist)+''.join(r.choice('0123456789')for i in range(8))
#创建原始通讯录
O_name=[]#名字
o=10
for i in range(o):
    O_name.append(name())

O_number=[]#号码
for i in range(o):
    O_number.append(number())

addressBook=dict(zip(O_name,O_number))#定义通讯录
func5(addressBook)#打印通讯录

print('''
|——————————————————————|
|----通讯录管理系统----|
|--1. 添加新的联系人---|
|--2. 删除已有联系人---|
|--3. 修改联系人号码---|
|--4. 查询个别联系人---|
|--5. 查询所有联系人---|
|--6. 再打印功能界面---|
|--7. 退出通讯录系统---|
|——————————————————————|
|——————————————————————|
|----from IPhone XR----|
 ''')


while 1:
    print("")
    n=input("请输入指令代码：")
    if not n.isdigit():
        print("输入错误，请按照指示输入！")
        continue
    item=int(n)#指令转换成数字
    if item==7:
        print(''' Σ（ﾟдﾟ|||）
Thanks for your using!''')
        break

    if item==1:                   #1.添加新的联系人
        print("|--1. 添加新的联系人---|")
        name=input("请输入联系人的姓名：")
        if name in addressBook:
            print("您输入的姓名已在通讯录中已存在-->>",name,":",addressBook[name])
            print("是否修改联系人资料?")
            modify=input("Please input 'y' for YES or 'n' for NO:")
            if modify=='y':
                userphone=input("请输入联系人号码：")
                if not userphone.isdigit():
                    print("输入错误，请按照指示输入！")
                    continue
                user=int(userphone)
                new_number=user
                while (user==int(addressBook[name])):
                    print("号码与修改前重复！")
                    retry=input("请重新输入/按空格键退出：")
                    if retry.isdigit():
                        new_number=int(retry)
                        addressBook[name]=new_number
                        continue
                    if  retry==' ':
                        print("取消修改！")
                        break
                    else:
                        print("输入指令无效！")
                        continue
                else:
                    addressBook[name]=new_number
                    print("联系人修改成功！")              
            elif modify=='n':
                print("取消修改成功！")
                continue
            else :
                print("指令无效！")
                continue
        else:
            userphone=input("请输入联系人号码：")
            if not userphone.isdigit():
                print("输入错误，请按照指示输入！")
                continue
            user=int(userphone)
            addressBook[name]=user
            print("联系人加入成功！")

    if item==2:                  #2.删除已有联系人
        print("|--2. 删除已有联系人---|")
        name=input("请输入联系人的姓名：")
        if name in addressBook:
            del addressBook[name]
            print("删除成功！")
            continue
        else:
            print("联系人不存在！")

    if item==3:                 #3.修改联系人号码
        print("|--3. 修改联系人号码---|")
        name=input("请输入联系人的姓名：")
        if name in addressBook:
            userphone=input("请输入联系人号码：")
            if not userphone.isdigit():
                print("输入错误，请按照指示输入！")
                continue
            user=int(userphone)
            new_number=user
            while (user==int(addressBook[name])):
                print("号码与修改前重复！")
                retry=input("请重新输入/按空格键退出：")
                if retry.isdigit():
                    new_number=int(retry)
                    addressBook[name]=new_number
                    continue
                if ' ' in retry:
                    print("取消修改！")
                    break
                else:
                    print("输入指令无效！")
                    continue
            else:
                addressBook[name]=new_number
                print("联系人修改成功！")
        else:
            print("联系人不存在！")

    if item==4:                 #4.查询个别联系人
        print("|--4. 查询个别联系人---|")
        name=input("请输入联系人的姓名：")
        if name in addressBook:
            print("联系人号码:",addressBook[name])
        else:
            print("联系人不存在！")

    if item==5:                 #5.查询所有联系人
        print("|--5. 查询所有联系人---|")
        func5(addressBook)

    if item==6:                 #6.再打印功能界面
        print('''
————————————————————————
|----通讯录管理系统----|
|--1. 添加新的联系人---|
|--2. 删除已有联系人---|
|--3. 修改联系人号码---|
|--4. 查询个别联系人---|
|--5. 查询所有联系人---|
|--6. 再打印功能界面---|
|--7. 退出通讯录系统---|
|——————————————————————|
|——————————————————————|
|----from IPhone XR----|
 ''')
    if not 1<=item<=7:
        print("输入指令超出范围！")