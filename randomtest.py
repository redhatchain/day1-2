# Author:JiaHongWang
# -*- coding utf-8 -*-
import random
count=1
random_num1=random.randint(0,100)
while count<=5:
    #random_num1=random.randint(0,100)
    number=input('请输入要猜的数字:')
    number=int(number)
    print('random_num1:' + str(random_num1))
    count+=1
    if random_num1==number:
        print('你猜对了')
        break
    elif number>random_num1:
        print('你猜大了')
    elif number<random_num1:
        print('你猜小了')







