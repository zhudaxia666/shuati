'''
**分析:**假设最长路径终点的是[i][j],则其最长路径值为nums1[i][j],则nums1[i][j]等于它上下左右四个数中，比它小的数中最长路径值最大的那一个+1
因此，我们可以从矩阵的最小值出发，其最长路径值为1，然后计算第二小的数的最长路径值，以此类推
'''
def longpath(n,mat):
    a = n
    dic = {}
    nums_max = 1
    if a == 0:
        nums_max = 0
    else:
        b = len(mat[0])
        for i in range(a):
            for j in range(b):
                dic[(i,j)] = mat[i][j]
        v =  dic.keys()
        nums1 = [[1 for i in range(b)] for j in range(a)]        
        dic = sorted(dic.items(),key = lambda x:x[1])
        # print(dic)
        for k in dic:
            i = k[0][0]
            j = k[0][1]
            if (i+1,j) in v and mat[i+1][j]<mat[i][j] and nums1[i][j]<nums1[i+1][j]+1:
                nums1[i][j] = nums1[i+1][j] + 1
            if (i,j+1) in v and mat[i][j+1]<mat[i][j] and nums1[i][j]<nums1[i][j+1]+1:
                nums1[i][j] = nums1[i][j+1] +1
            if (i-1,j) in v and mat[i-1][j]<mat[i][j] and nums1[i][j]<nums1[i-1][j]+1:
                nums1[i][j] = nums1[i-1][j] +1
            if (i,j-1) in v and mat[i][j-1]<mat[i][j] and nums1[i][j]<nums1[i][j-1]+1:
                nums1[i][j] = nums1[i][j-1] + 1    
            nums_max = max(nums_max,nums1[i][j])              
    return nums_max
n=int(input())
m=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
print(longpath(n,mat))
