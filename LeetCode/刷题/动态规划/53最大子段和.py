'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        max_sub_sum = nums[0]
        for num in nums:
            sum += num
            if sum > max_sub_sum:
                max_sub_sum = sum
            if sum < 0:
                sum = 0
        return max_sub_sum

#dp
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        max_res=dp[0]
        for i in range(1,len(nums)):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
            if max_res<dp[i]:
                max_res=dp[i]
        return max_res
#如果dp[i-1]>0 dp[i]=dp[i-1]+nums[i]  else dp[i]=nums[i]
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        temp=nums[0]
        max_=temp
        for i in range(1,len(nums)):
            if temp>0:                
                temp+=nums[i]
            else:
                temp=nums[i]
            max_=max(max_,temp)
        return max_