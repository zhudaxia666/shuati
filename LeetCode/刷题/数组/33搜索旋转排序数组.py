'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。


找到旋转的下标 rotation_index ，也就是数组中最小的元素。二分查找在这里可以派上用场。
在选中的数组区域中再次使用二分查找。
'''
class Solution:
    def search(self,nums,target):
        n=len(nums)
        if n==0:
            return -1
        if n==1:
            return -1 if nums[0]!=target else 0
        rotateindex=self.findrote(nums,0,n-1)
        if nums[rotateindex]==target:
            return rotateindex
        if rotateindex==0:
            return self.search1(nums,0,n-1,target)
        if target<nums[0]:
            return self.search1(nums,rotateindex,n-1,target)
        return self.search1(nums,0,rotateindex,target)

    def findrote(self,nums,left,right):
        if nums[left]<nums[right]:
            return 0
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>nums[mid+1]:
                return mid+1
            else:
                if nums[mid]<nums[left]:
                    right=mid-1
                else:
                    left=mid+1
    def search1(self,nums,left,right,target):
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
                
        def search(left, right):
            """
            Binary search
            """
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1
        
        n = len(nums)
        
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1 
        
        rotate_index = find_rotate_index(0, n - 1)
        
        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)