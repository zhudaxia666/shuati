'''
在二维平面上有一个无限的网格图形，初始状态下，所有的格子都是空白的。现在有n个操作，
每个操作是选择一行或一列，并在这行或这列上选择两个端点网格，把以这两个网格为端点的区间内的所有网格染黑
（包含这两个端点）。问经过n次操作之后，共有多少个格子被染黑，显然在众多操作中，很容易重复染色同一个格子，
这个时候只计数一次。
'''
def gezi(x1,y1,x2,y2):
    d=[]
    if x1==x2:
        s1=str(x1)
        if y1<=y2:
            for i in range(y1,y2+1,1):
                s=str(i)
                d.append(s1+','+s)
        else:
            for i in range(y2,y1+1,1):
                s=str(i)
                d.append(s1+','+s)
        if y1<=y2:
            for i in range(x1,x2+1,1):
                s=str(i)
                d.append(s+','+s1)
        else:
            for i in range(x2,x1+1,1):
                s=str(i)
                d.append(s+','+s1)
    return len(d)




