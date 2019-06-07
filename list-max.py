# Author:JiaHongWang
# -*- coding utf-8 -*-
nums=[19,20,33,55,56,77]
index=0
index_id=0
max_num=0

for num in nums:
    if num>max_num:
        max_num=num
        index=index_id
    index_id+=1
print('max_num:%d,nums[%d]'% (max_num,index))




