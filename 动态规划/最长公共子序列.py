'''
子串要求字符必须是连续的，但是子序列就不是这样。最长公共子序列是一个十分实用的问题，它可以描述两段文字之间的“相似度”，
即它们的雷同程度，从而能够用来辨别抄袭。对一段文字进行修改之后，计算改动前后文字的最长公共子序列，将除此子序列外的部分提取出来，
这种方法判断修改的部分，往往十分准确。
解法就是用动态回归的思想，一个矩阵记录两个字符串中匹配情况，若是匹配则为左上方的值加1，否则为左方和上方的最大值。
一个矩阵记录转移方向，然后根据转移方向，回溯找到最长子序列。

'''
def LCS(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1]+1
            else:
                res[i][j] = max(res[i-1][j],res[i][j-1])
    return res[-1][-1]
print(LCS("helloworld","loop"))

# 原文链接：https://blog.csdn.net/ggdhs/article/details/90713154


def Lcs(s1,s2):
    m=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    d=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                m[i+1][j+1]=m[i][j]+1
                d[i+1][j+1]='ok'
            elif m[i+1][j]>m[i][j+1]:
                m[i+1][j+1]=m[i+1][j]
                d[i+1][j+1]='left'
            else:
                m[i+1][j+1]=m[i][j+1]
                d[i+1][j+1]='up'
    return m,d
def printlcs(d,s1,i,j):
    if i==0 or j==0:
        return
    if d[i][j]=='ok':
        printlcs(d,s1,i-1,j-1)
        print(s1[i-1],end='')
    elif d[i][j]=='left':
        printlcs(d,s1,i,j-1)
    else:
        printlcs(d,s1,i-1,j)

import numpy as np
def Lcs1(s1,s2):
    m=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    d=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                m[i+1][j+1]=m[i][j]+1
                d[i+1][j+1]='ok'
            elif m[i+1][j]>m[i][j+1]:
                m[i+1][j+1]=m[i+1][j]
                d[i+1][j+1]='left'
            else:
                m[i+1][j+1]=m[i][j+1]
                d[i+1][j+1]='up'
    l1,l2=len(s1),len(s2)
    print(np.array(d))
    s=[]
    while m[l1][l2]!=0:
        if d[l1][l2]=='ok':
            s.append(s1[l1-1])
            l1-=1
            l2-=1
        elif d[l1][l2]=='left':
            l2-=1
        else:
            l1-=1
    s.reverse()
    return ''.join(s)

a='abdfg'
b='abcdfe'
print(Lcs1(a,b))

# c,flag=Lcs(a,b)
# for i in c:
#     print(i)
# # print('')
# printlcs(flag,a,len(a),len(b))
# # print('')
