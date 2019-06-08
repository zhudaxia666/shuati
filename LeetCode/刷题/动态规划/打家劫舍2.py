'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例 1:
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

相比较于打家劫舍1变化的是首尾之间的内部关系，所以只需分情况讨论，可以偷第一家,这时一定不能偷最后一家和不能偷第一家，可以偷最后一家的情况
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        dp1=[0]*(len(nums)-1)
        dp2=[0]*(len(nums)-1)
        dp1[0]=nums[0]
        dp2[0]=nums[1]
        dp1[1]=max(nums[1],nums[0])
        dp2[1]=max(nums[2],nums[1])
        for i in range(2,len(nums)-1):
            dp1[i]=max(dp1[i-2]+nums[i],dp1[i-1])
        for i in range(2,len(nums)-1):
            dp2[i]=max(dp2[i-2]+nums[i+1],dp2[i-1])
        return max(dp1[-1],dp2[-1])


'''
,跟上一题打家劫舍一样的方法，只多了一个判断，判断两种情况，偷第一家或不偷第一家，重新复制了两个数组
'''
class Solution1:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        if l <= 2:
            return max(nums)
        nums1 = nums[:l-1]
        nums2 = nums[1:l]
        ans1 = self.robhelper(nums1)
        ans2=self.robhelper(nums2)
        return max(ans1,ans2)

    def robhelper(self,nums):
        last = 0
        now = 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now