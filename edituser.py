# Author:JiaHongWang
# -*- coding utf-8 -*-
users=[]
users.append((1,'kk',39,'18500000001'))
users.append((2,'bb',30,'18500000002'))
users.append((3,'dd',32,'18500000003'))
#定义title
tp_title='|{0:^10s}|{1:^10s}|{2:^5s}|{3:^11s}|'
colums_title=('ID','NAME','AGE','TEL')
title=tp_title.format('ID','NAME','AGE','TEL')
tp_body='|{0:^10d}|{1:^10s}|{2:^5d}|{3:^11s}|'
print(title)
print('-'* len(title))
uid=input('请输入要修改的用户ID:')
uid=int(uid)
exists_users=None
for user in users:
    if uid==user[0]:
        exists_users=user
        break
if exists_users:
    prompt=input('请输入要添加的信息(name,age,tel):')
    nodes=prompt.split(',')
    if len(nodes)!=3:
        print('输入信息错误')
    else:
        users.remove(exists_users)
        nodes[1]=int(nodes[1])
        users.append((uid,)+tuple(nodes))
else:
    print('用户不存在')
print(users)
