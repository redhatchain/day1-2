
# Author:JiaHongWang
# -*- coding utf-8 -*-

num1=[1,2,3,3,4,4,5,6,6,7,8,9,12,13]
num2=[1,2,3,4,5,6,6,3,23,34,45,66,77]
num3=[]
for nums in num1:
    if nums in num1 and nums not in num3:
        num3.append(nums)
print (num3)