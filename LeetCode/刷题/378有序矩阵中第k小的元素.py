'''
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。
示例:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。
'''
'''
思路：二分查找的思想：初始时，最小值为为第一个元素l，最大值为最后一个元素h，
中值mid=(l+h)//2,计算mid的位置，是第j小的数
当j<k时，l=mid+1,否则h=mid  。重复以上几步直到不符合l<h
'''
def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n, m = len(matrix), len(matrix[0])
        l, h = matrix[0][0], matrix[n-1][m-1]
        
        while l < h:
            count = 0
            mid = l + (h-l)//2
            for i in range(n):
                j = m-1
                while j>=0 and matrix[i][j]>mid:
                    j -= 1               
                count += j+1
                #print(count, k)
            if count>=k:
                h = mid
            else:
                l = mid + 1
        return l