# Author:JiaHongWang
# -*- coding utf-8 -*-
#添加用户


users=[]
users.append((1,'kk',39,'18500000001'))
users.append((2,'kk',30,'18500000002'))
users.append((3,'kk',32,'18500000003'))
#定义title
tp_title='|{0:^10s}|{1:^10s}|{2:^5s}|{3:^11s}|'
colums_title=('ID','NAME','AGE','TEL')
title=tp_title.format('ID','NAME','AGE','TEL')
tp_body='|{0:^10d}|{1:^10s}|{2:^5d}|{3:^11s}|'
user_id=0
print(title)
print('-'* len(title))
while True:
    prompt=input('请输入要添加的信息(name,age,tel):')
    nodes=prompt.split(',')
    if len(nodes)!=3:
        print('输入信息错误')

    else:
        uid=0
        nodes[1]=int(nodes[1])
        for user in users:
            if uid<user[0]:
                uid=user[0]
        users.append((uid+1,)+tuple(nodes))
    print(users)








