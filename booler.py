# Author:JiaHongWang
# -*- coding utf-8 -*-
n=1
while n<=3:

    year = input('请输入一个年份：')
    year = int(year)
    if year%4==0 and year%100!=0:
        print('这个年份是闰年:'+ str(year))
        n+=1
    elif year%400==0:
            print('这个年份是在闰:' + str(year))
            n+=1
    else:
        print('这个年份不是闰年'+ str(year))
        n+=1





