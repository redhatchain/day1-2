
# Author:JiaHongWang
# -*- coding utf-8 -*-
users=[]
users.append((1,'kk',39,'18500000001'))
users.append((2,'aa',30,'18500000002'))
users.append((3,'bb',32,'18500000003'))
#定义title
tp_title='|{0:^10s}|{1:^10s}|{2:^5s}|{3:^11s}|'
colums_title=('ID','NAME','AGE','TEL')
title=tp_title.format('ID','NAME','AGE','TEL')
tp_body='|{0:^10d}|{1:^10s}|{2:^5d}|{3:^11s}|'

while True:
    txt=input('请输入要执行的动作(list/add/edit/delete/find):')
    if txt=='list':
        for i in users:
            print(title)
            print('-'* len(title))
            print(tp_body.format(i[0],i[1],i[2],i[3]))
    elif txt=='add':
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
            print('添加成功')
    elif txt=='delete':

        uid=input('请输入要删除的ID:')
        uid=int(uid)
        for user in users:
            if uid==user[0]:
                users.remove(user)
                break
    elif txt=='edit':
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
    elif txt=='find':
        name=input('请输入要查找的用户名：')
        for user in users:
            if name==user[1]:
                print(title)
                print('-'* len(title))
                print(tp_body.format(user[0],user[1],user[2],user[3]))

