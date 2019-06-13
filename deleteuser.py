# Author:JiaHongWang
# -*- coding utf-8 -*-
users=[]
users.append((1,'aa',39,'18500000001'))
users.append((2,'bb',30,'18500000002'))
users.append((3,'cc',32,'18500000003'))
#定义title
tp_title='|{0:^10s}|{1:^10s}|{2:^5s}|{3:^11s}|'
colums_title=('ID','NAME','AGE','TEL')
title=tp_title.format('ID','NAME','AGE','TEL')
tp_body='|{0:^10d}|{1:^10s}|{2:^5d}|{3:^11s}|'
print(title)
print('-'* len(title))
#删除记录
uid=input('请输入要删除的ID:')
uid=int(uid)
for user in users:
    if uid==user[0]:
        users.remove(user)
        break
print(users)




