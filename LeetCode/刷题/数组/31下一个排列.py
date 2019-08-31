'''
先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
再找出另一个最大索引 l 满足 nums[l] > nums[k]；
交换 nums[l] 和 nums[k]；
最后翻转 nums[k+1:]。
'''
#
class Solution:
    def nextPermutation(self,nums):
        index=len(nums)-1
        def reverse(nums,i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                index=i-1
                break
        if index==len(nums)-1:
            reverse(nums,0,len(nums)-1)
            return
        else:
            for i in range(len(nums)-1,index,-1):
                if nums[index]<nums[i]:
                    nums[index],nums[i]=nums[i],nums[index]
                    break
            reverse(nums,index+1,len(nums)-1)

def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    index=len(nums)-1
    for i in range(len(nums)-1,0,-1):
        if nums[i-1]<nums[i]:
            index=i-1
            break
    if index==len(nums)-1:
        return nums[::-1]
    else:
        for i in range(len(nums)-1,index,-1):
            if nums[index]<nums[i]:
                nums[index],nums[i]=nums[i],nums[index]
                nums[index+1],nums[-1]=nums[-1],nums[index+1]
        return nums
        
print(nextPermutation([2,3,1]))