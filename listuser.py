
# Author:JiaHongWang
# -*- coding utf-8 -*-
users=[]
users.append((1,'kk',39,'18500000001'))
users.append((2,'kk',30,'18500000002'))
users.append((3,'kk',32,'18500000003'))
#定义title
tp_title='|{0:^10s}|{1:^10s}|{2:^5s}|{3:^11s}|'
colums_title=('ID','NAME','AGE','TEL')
title=tp_title.format('ID','NAME','AGE','TEL')
tp_body='|{0:^10d}|{1:^10s}|{2:^5d}|{3:^11s}|'
print(title)
print('-'* len(title))
for i in users:
    print(tp_body.format(i[0],i[1],i[2],i[3]))
