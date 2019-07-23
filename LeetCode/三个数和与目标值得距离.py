''''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
'''

# 先排序再双指针，双指针的移动条件是当sum>target时右指针左移，当sum<target左指针右移，
# 等于直接返回答案，这样可以不断找到接近target的数。每次移动后都判断一下就好了。
def Sum(nums,target):
    minabs = 1000000
    nums.sort()
    for i in range(len(nums)-1):
        if i==0 or nums[i]!=nums[i-1]:
            l = i+1
            r = len(nums)-1
            while(l<r):
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:#指针移动到下一个不同的数字
                    return target
                chazhi = abs(sum-target)
                if chazhi<minabs:
                    minabs = chazhi
                    ans = sum
                if sum>target:
                    r-=1
                    while(l<r and nums[r]==nums[r+1]):
                        r-=1
                else:
                    l+=1
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
    return ans

def ThreeSum(nums,target):
    minx=1000000
    nums.sort()
    for i in range(len(nums)-1):
        if i ==0 or nums[i]!=nums[i-1]:
            left=i+1
            right=len(nums)-1
            while(left<right):
                sum=nums[i]+nums[left]+nums[right]
                if sum==target:
                    return 0
                chazhi=abs(sum-target)
                if chazhi < minx:
                    minx=chazhi
                    ans=sum
                if sum>target:
                    right-=1
                    while(left<right and nums[right]==nums[right+1]):
                        right-=1
                else:
                    left+=1
                    while(left<right and nums[left]==nums[left-1]):
                        left+=1
    return ans



target=1
nums=[-1,2,1,-4]
print(ThreeSum(nums,target))