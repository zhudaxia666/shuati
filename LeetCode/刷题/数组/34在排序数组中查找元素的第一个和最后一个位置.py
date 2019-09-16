'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        if n==0:
            return [-1,-1]
        if n==1:
            return [-1,-1] if nums[0]!=target else [0,0]
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                b=mid
                e=mid
                while b>0:
                    if nums[b-1]==target:
                        b=b-1
                    else:
                        break
                while e<n-1:
                    if nums[e+1]==target:
                        e=e+1
                    else:
                        break
                return [b,e]
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return [-1,-1]