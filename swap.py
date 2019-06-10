# Author:JiaHongWang
# -*- coding utf-8 -*-
list1=[3,21,13,45,33,29]
tmp=0
#index1=1
for j in range(len(list1)-1):
    for index2 in range(len(list1)-1):
        if list1[index2]>list1[index2+1]:
            '''
            tmp=list1[index2]
            list1[index2]=list1[index1]
            list1[index1]=tmp
            '''
            list1[index2],list1[index2+1]=list1[index2+1],list1[index2]
    #    index1+=1
print(list1)
