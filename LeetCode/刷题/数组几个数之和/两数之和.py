'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
'''
class Solution:
    def twoSum(self, nums, target):
        hashmap={}
        for key,value in enumerate(nums):
            result=target-value
            if result in hashmap:
                return [hashmap[result],key]
            hashmap[value]=key
        return None

a=Solution()
nums = [2,7,11,15]
target = 9
print(a.twoSum(nums,target))
