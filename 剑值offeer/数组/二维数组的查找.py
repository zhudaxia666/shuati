'''
把每一行看成有序递增的数组，
利用二分查找，
通过遍历每一行得到答案，
时间复杂度是nlogn
'''
class Solution:
    # array 二维列表
    #每一行都看成是一个有序数组，利用二分查找
    def Find(self, target, array):
        row=len(array)
        for i in range(row):
            left=0
            right=len(array[i])-1
            while left<=right:
                mid=int((left+right)/2)
                if array[i][mid]<target:
                    left=mid+1
                elif array[i][mid]>target:
                    right=mid-1
                else:
                    return 1
        return 0
'''
另外一种思路是：
利用二维数组由上到下，由左到右递增的规律，
那么选取右上角或者左下角的元素a[row][col]与target进行比较，
当target小于元素a[row][col]时，那么target必定在元素a所在行的左边,
即col--；
当target大于元素a[row][col]时，那么target必定在元素a所在列的下边,
即row++；
'''
class Solution2:
    # array 二维列表
    def Find(self, target, array):
        row_len=0
        col_len=len(array[0])-1
        while row_len<len(array) and col_len>=0:
            if target==array[row_len][col_len]:
                return True
            elif target<array[row_len][col_len]:
                col_len-=1
            else:
                row_len+=1
        return False
'''
思路三
'''
class Solution1:
    # array 二维列表
    #每一行都看成是一个有序数组，利用二分查找
    def Find(self, target, array):
        n=len(array)
        for i in range(n):
            if target in array[i]:
                return 1
        return 0