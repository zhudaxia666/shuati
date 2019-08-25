'''
LCS问题就是求两个字符串最长公共子串的问题。解法就是用一个矩阵来记录两个字符串中所有位置的两个字符之间的匹配情况，
若是匹配则为1,否则为0。然后求出对角线最长的1的序列，其对应的位置就是最长匹配子串的位置。
'''
def LCS(s1,s2):
    m=[[0]*(len(s2)+1) for i in range(len(s1)+1)]
    mmax=0
    p=0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                m[i+1][j+1]=m[i][j]+1
                if m[i+1][j+1]>mmax:
                    mmax=m[i+1][j+1]
                    p=i+1
    return s1[p-mmax:p],mmax
# def lcs(s1,s2):
#     len1=len(s1)
#     len2=len(s2)
#     res=[[0 for i in range(len1+1)] for j in range(len2+1)]
#     result=0
#     for i in range(1,len2+1):
#         for j in range(1,len1+1):
#             if s1[j-1]==s2[i-1]:
#                 res[i][j]=res[i-1][j-1]+1
#                 result+=max(result,res[i][j])
#     return result

# print(lcs('bacdfe','eacdw'))
print(LCS("helloworld","loop"))
#添加字符
'''
牛牛手里有一个字符串A，羊羊的手里有一个字符串B，B的长度大于等于A，所以牛牛想把A串变得和B串一样长，这样羊羊就愿意和牛牛一起玩了。
而且A的长度增加到和B串一样长的时候，对应的每一位相等的越多，羊羊就越喜欢。比如"abc"和"abd"对应相等的位数为2，为前两位。
牛牛可以在A的开头或者结尾添加任意字符，使得长度和B一样。现在问牛牛对A串添加完字符之后，不相等的位数最少有多少位？
'''
def lcs11(a,b):
    len1=len(a)
    len2=len(b)
    nmax=0
    p=0
    res=[[0]*(len(b)+1) for _ in range(len1)]
    for i in range(len1):
        for j in range(len2):
            if a[i]==b[j]:
                res[i+1][j+1]=res[i][j]+1
                if res[i+1][j+1]>nmax:
                    nmax=res[i+1][j+1]
                    p=i+1
    return len1-nmax,a[p-nmax:p]
print(lcs11('abe','cabc'))

