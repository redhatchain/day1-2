
# Author:JiaHongWang
# -*- coding utf-8 -*-

todo=[]
while True:
    promt=input("请输入任务/do:")
    if promt=='do':
        if len(todo)>0:

            print('请完成任务：%s' % todo.pop(0))
        else:
            print('所有任务已完成')
            break

    else:

        todo.append(promt)


