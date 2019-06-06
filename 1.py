# Author:JiaHongWang
# -*- coding utf-8 -*-

total=0
n=0
number=''
agv=0
while number!='exit':
    number = input('请输入一个数字或exit:')
    if number!='exit':
        n+=1
        number=float(number)
        total+=number

if n !=0:
    agv=float(total/n)
    print('数字和:'+ str(total))
    print('数字的平均数：'+ str(agv))
else:
    print('数字和是:',total)
    print('平均数是：',agv)


