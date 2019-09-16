'''
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： 
counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
示例:
输入: [5,2,6,1]
输出: [2,1,1,0] 
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

思路：
将给定数组从最后一个开始，用二分法插入到一个新的数组，这样新数组就是有序的，
那么此时该数字在新数组中的坐标就是原数组中其右边所有较小数字的个数，时间复杂度为O（nlogn）
'''
class Solution:
    def bisearch(self,tmp,a):
        left = 0
        right = len(tmp)
        while left < right:
            mid = (left + right) //2
            if tmp[mid] <a:
                left = mid +1
            else:
                right = mid
        return left
    
    def countSmaller(self, nums):
        ans=[]
        tmp = []
    
        for i in range(len(nums)-1,-1,-1):
            pos = self.bisearch(tmp, nums[i])
            ans.append(pos)
            tmp.insert(pos,nums[i])
        ans.reverse()
        # print(tmp)
        return ans
a=Solution()
a.countSmaller([5,2,6,1])
