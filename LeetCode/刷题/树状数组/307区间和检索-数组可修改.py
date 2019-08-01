'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。
示例:
Given nums = [1, 3, 5]
sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

说明:
数组仅可以在 update 函数下进行修改。
你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。
'''
#使用树状数组
class IndexTree(object):
    def __init__(self,nums):
        n=len(sums)
        sum=[0]*(n+1)
        for i in range(1,n+1):
            sum[i]=sum[i-1]+nums[i-1]
        self.sum=[0]*(n+1)
        for i in range(1,n+1):
            self.sums[i]=sum[i]-sum[i-(i&-i)]
    def getsum(self,i):
        res=0
        while i>0:
            res+=self.sums[i]
            i-=(i&-i)
        return res
    def update(self,i,val):
        n=len(self.sum)-1
        while i<=n:
            self.sum[i]+=val
            i+=(i&-i)
class Numarray:
    def __init__(self,nums):
        self.tree=IndexTree(nums)
        self.nums=nums
    def updata(self,i,val):
        diff=val-self.nums[i]
        nums[i]=val
        self.tree.update(i+1,diff)
    def sumRange(self,i,j):
        return self.tree.getsum(j+1)-self.tree.getsum(i)

#方法2
class FenwickTree2:
    def __init__(self,n):
        self._sums = [0 for _ in range(n+1)]

    def update(self,i,delta):
        while i < len(self._sums):
            self._sums[i] += delta
            i += i & -i
    
    def query(self,i):
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i & -i
        return s

class NumArray2:

    def __init__(self, nums: List[int]):
        self._nums = nums
        self._tree = FenwickTree(len(nums))
        for i in range(len(nums)):
            self._tree.update(i+1,nums[i])

    def update(self, i: int, val: int) -> None:
        self._tree.update(i+1,val-self._nums[i])
        self._nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self._tree.query(j+1)-self._tree.query(i)
