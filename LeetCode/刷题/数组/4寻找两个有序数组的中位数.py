'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''
'''
思路：
两个有序数组求中位数，问题一般化为，求两个有序数组的第k个数，当k = (m+n)/2时为原问题的解。
怎么求第k个数？分别求出第一个和第二个数组的第 k / 2个数 a 和 b，然后比较 a 和 b，当a < b ，
说明第 k 个数位于 a数组的第 k / 2个数后半段，或者b数组的 第 k / 2 个数前半段，问题规模缩小了一半，然后递归处理就行。
时间复杂度是 O(log(m+n))
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findkth(nums1,nums2,k):
            m=len(nums1)
            n=len(nums2)
            if m==0:
                return nums2[k-1]
            if n==0:
                return nums1[k-1]
            if k==1:
                return min(nums1[0],nums2[0])
            
            mid=k//2
            a=float("inf")
            b=float("inf")
            
            if mid<=m:
                a=nums1[mid-1]
            if mid<=n:
                b=nums2[mid-1]
            if a<b:
                return findkth(nums1[mid:],nums2,k-mid)
            else:
                return findkth(nums1,nums2[mid:],k-mid)
        m=len(nums1)
        n=len(nums2)
        
        if m==0 and n==0:
            return 0.0
        total=m+n
        if total%2==1:
            return findkth(nums1,nums2,total//2+1)*1.0
        else:
            a=findkth(nums1,nums2,total//2)
            b=findkth(nums1,nums2,total//2+1)
            return (a+b)/2.0