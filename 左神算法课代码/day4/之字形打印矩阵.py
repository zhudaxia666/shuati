'''
设置两个指针A和B，刚开始都指向m[0][0]位置，然后A向右移动，B向左移动，当A移动到最右面，向下移动。当B移动到最下面，向右移动。设置一个flag，标志打印斜线的方向。
终止条件是A行标等于矩阵行货B列标等于矩阵列数
'''
def zhiziprint(matrix):
    tr=0
    tc=0
    dr=0
    dc=0
    endr=len(matrix)-1
    endc=len(matrix[0])-1
    res=[]
    flag=-1
    while tr!=endr+1:
        printm(matrix,tr,tc,dr,dc,res,flag)
        if tc==endc:#A到最右边，往下走
            tr+=1
        else:
            tc+=1
        if dr==endr:#B到最下端往右走
            dc+=1
        else:
            dr+=1
        flag=-flag
    print(res)
def printm(matrix,tr,tc,dr,dc,res,flag):
    if flag>0:
        while tr!=dr+1:#斜着打印
            res.append(matrix[tr][tc])
            tr+=1
            tc-=1
    else:
        while dr!=tr-1:
            res.append(matrix[dr][dc])
            dr-=1
            dc+=1
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
zhiziprint(matrix)
