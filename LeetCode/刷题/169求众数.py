'''
我们假设将第一个数字作为众数看待，遍历数组，若元素 == 当前众数res则count += 1，否则count -= 1;
在下次count == 0时，意味着当前众数res的数量为已遍历元素一半；这种情况下，剩余数组众数仍等于原数组众数（因为最坏的情况是已遍历数组中一半是数组众数，一半是非众数）。
因此，在每次count == 0时，记录当前数字为当前众数，当遍历完整个数组时，留下的res一定为整个数组的众数（最坏情况是在最后一个元素才找到众数，前面的count全部抵消）。
'''
class Solution1:
    def majorityElement(self, nums: [int]) -> int:
        count = 0
        for num in nums:
            if not count: res = num
            count += 1 if num == res else -1
        return res

#摩尔投票算法
class Solution(object):
    def majorityElement(self,nums): 
        tmp=nums[0]
        count=1
        for i in range(1,len(nums)):
            if count==0:
                tmp=nums[i]
            count=count+1 if nums[i]==tmp else count-1
        return tmp