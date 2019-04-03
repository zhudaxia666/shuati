'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
思路：
创建双向队列，遍历数组，奇数前插入，偶数后插入
'''
#队列
class Solution1:
    def reOrderArray(self, array):
        # write code here
        from collections import deque
        odd = deque()
        x = len(array)
        for i in range(x):
            if array[x-i-1]%2 != 0:
                odd.appendleft(array[x-i-1])
            if array[i]%2 == 0:
                odd.append(array[i])
        return list(odd)


#列表
class Solution2:
    def reOrderArray(self, array):
        res=[]
        l=len(array)
        for i in range(l):
            if array[l-i-1]%2!=0:
                res.insert(0,array[l-i-1])
            if array[i]%2==0:
                res.append(array[i])
        return res
#不开辟空间
class Solution3:
    def reOrderArray(self, array):
        # write code here
        boarder = -1
        for idx in range(len(array)):
            if array[idx] % 2:
                boarder += 1
                array.insert(boarder, array.pop(idx))
        return array