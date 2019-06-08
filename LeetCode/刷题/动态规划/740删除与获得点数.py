'''
给定一个整数数组 nums ，你可以对它进行一些操作。
每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。
开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
示例 1:
输入: nums = [3, 4, 2]
输出: 6
解释: 
删除 4 来获得 4 个点数，因此 3 也被删除。
之后，删除 2 来获得 2 个点数。总共获得 6 个点数。
示例 2:
输入: nums = [2, 2, 3, 3, 3, 4]
输出: 9
解释: 
删除 3 来获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
'''
#思路：改成打家劫舍的问题，取最大的数m建立一个长度为m+1的数组。然后将nums映射到这个数组上，相同的相加在一起，然后就是打家劫舍的问题
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if( len(nums)==0 ): return 0
        if( len(nums)==1 ): return nums[0]
        max_v = max( nums )
        a = [0]*(max_v+1)
        
        for num in nums:
            a[num] += num
            
        return_ans = [0]*(max_v+1)
        return_ans[1] = a[1]
        return_ans[2] = max( a[1], a[2] )
        
        
        for i in range(3,len(a),1):
            v = a[i]
            return_ans[i] = max( return_ans[i-1], return_ans[i-2]+a[i] )
            
        return return_ans[-1]


    class Solution1(object):
        def deleteAndEarn(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if not nums or len(nums)==0:
                return 0
            if len(nums)==1:
                return nums[0]
            dp = [0]*(max(nums)+1)
            for num in nums:
                dp[num]+=num
            return self.Rob(dp)

        def Rob(self,nums):
            nums[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                nums[i] = max(nums[i-1],nums[i-2]+nums[i])
            return nums[-1]