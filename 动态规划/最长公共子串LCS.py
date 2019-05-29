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
print(LCS('bacdfe','eacdw'))