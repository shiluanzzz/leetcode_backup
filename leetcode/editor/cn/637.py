# -*- coding:utf-8 -*-
# __author__ = "shiluanzzz"

# 二叉树的层平均值

def solve(root):
    q=[root]
    result=[]
    while q:
        new_q=[]
        avg=0
        count=0
        while q:
            item=q.pop()
            if item:
                avg+=item
                count+=1
                new_q.append(item.left)
                new_q.append(item.right)
            else:
                continue
        q=new_q
        result.append(avg/count)
    return result