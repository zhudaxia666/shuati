'''
对于序列S和T, 它们之间的距离定义为: 对二者其一进行几次以下操作:
 1, 删除一个字符; 2, 插入一个字符; 3, 改变一个字符. 每进行一次操作, 计数增加1.
将S和T变为相等序列的最小计数就是两者的编辑距离(edit distance)或者叫相似度
'''
'''
原理分析：
假设序列S和T的长度分别为m和n, 两者的编辑距离表示为edit[m][n]. 则对序列进行操作时存在以下几种情况:

a, 当S和T的末尾字符相等时, 对末尾字符不需要进行上述定义操作中(亦即"编辑")的任何一个, 也就是不需要增加计数. 则满足条件: edit[m][n] = edit[m - 1][n - 1].
b, 当S和T的末尾字符不相等时, 则需要对两者之一的末尾进行编辑, 相应的计数会增加1.
    b1, 对S或T的末尾进行修改, 以使之与T或S相等, 则此时edit[m][n] = edit[m - 1][n - 1] + 1;
    b2, 删除S末尾的元素, 使S与T相等, 则此时edit[m][n] = edit[m - 1][n] + 1;
    b3, 删除T末尾的元素, 使T与S相等, 则此时edit[m][n] = edit[m][n - 1] + 1;
    b4, 在S的末尾添加T的尾元素, 使S和T相等, 则此时S的长度变为m+1, 但是此时S和T的末尾元素已经相等, 只需要比较S的前m个元素与T的前n-1个元素, 所以满足edit[m][n] = edit[m][n - 1] + 1;
    b5, 在T的末尾添加S的尾元素, 使T和S相等, 此时的情况跟b4相同, 满足edit[m][n] = edit[m - 1][n] + 1;
c, 比较特殊的情况是, 当S为空时, edit[0][n] = n; 而当T为空时, edit[m][0] = m; 这个很好理解, 例如对于序列""和"abc", 则两者的最少操作为3, 即序列""进行3次插入操作, 或者序列"abc"进行3次删除操作.
所以, 以上我们不难推出编辑距离的动态规划方程为:

, 其中
edit[i][j]=   0       i=0,j=0
        j       i=0,j>0
        i       i>0,j=0
    min{edit[i-1][j]+1,edit[i][j-1]+1,edit[i-1][j-1]+flag}  i>0.j>0
    flag=0  A[i]=B[j]
         1  A[i]!=B[j]
''' 
#动态规划算法中的递归实现
def editdistance(A,B):
    if not A or not B:
        return -1
    return edit(A,B,len(A)-1,len(B)-1)
def edit(a,b,len1,len2):
    if len1<0 or len2<0:
        return 1
    elif a[len1]==b[len2]:
        return edit(a,b,len1-1,len2-1)
    else:
        return min(edit(a,b,len1-1,len2)+1,min(edit(a,b,len1,len2-1)+1,edit(a,b,len1-1,len2-1)+1))

#动态规划中的回溯法
def edit1(a,b):
    if not a or not b:
        return -1
    mat=[[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0 and j == 0:
                mat[i][j] = 0
            # 初始化矩阵
            elif i == 0 and j > 0:
                mat[0][j] = j
            elif i > 0 and j == 0:
                mat[i][0] = i
            # flag
            elif a[i - 1] == b[j - 1]:
                mat[i][j] = min(mat[i - 1][j - 1], mat[i][j - 1] + 1, mat[i - 1][j] + 1)
            else:
                mat[i][j] = min(mat[i - 1][j - 1] + 1, mat[i][j - 1] + 1, mat[i - 1][j] + 1)
    return mat[len(a)][len(b)]
def eidt_1(s1, s2):
    # 矩阵的下标得多一个
    len_str1 = len(s1) + 1
    len_str2 = len(s2) + 1
 
    # 初始化了一半  剩下一半在下面初始化
    matrix = [[0] * (len_str2) for i in range(len_str1)]
 
    for i in range(len_str1):
        for j in range(len_str2):
            if i == 0 and j == 0:
                matrix[i][j] = 0
            # 初始化矩阵
            elif i == 0 and j > 0:
                matrix[0][j] = j
            elif i > 0 and j == 0:
                matrix[i][0] = i
            # flag
            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1] + 1, matrix[i - 1][j] + 1)
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j] + 1)
    return matrix[len_str1 - 1][len_str2 - 1]

print(edit1('cfe','coffe'))