'''
两个有序数组求中位数，问题一般化为，求两个有序数组的第k个数，当k = (m+n)/2时为原问题的解。
 怎么求第k个数？分别求出第一个和第二个数组的第 k / 2个数 a 和 b，然后比较 a 和 b，当a < b ，
 说明第 k 个数位于 a数组的第 k / 2个数后半段，或者b数组的 第 k / 2 个数前半段，问题规模缩小了一半，然后递归处理就行。
  时间复杂度是 O(log(m+n))
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)

        #处理任何一个nums为空数组的情况
        if m==0:
            if n%2!=0:
                return 1.0*nums2[n//2]
            return (nums2[n//2]+nums2[n//2-1])/2.0
        if n==0:
            if m%2!=0:
                return 1.0*nums1[m//2]
            return (nums1[m//2]+nums1[m//2-1])/2.0

        s=m+n
        #总数为奇数，找第 total / 2 + 1 个数
        if (s%2)==1:
            return self.find_kth(nums1,0,nums2,0,s//2+1)
        # //总数为偶数，找第 total / 2 个数和第total / 2 + 1个数的平均值
        else:
            return (self.find_kth(nums1,0,nums2,0,s//2)+self.find_kth(nums1,0,nums2,0,s//2+1))/2.0
    # //寻找a 和 b 数组中，第k个数字
    def find_kth(self,a,a_begin,b,b_begin,k):
        # //当a 或 b 超过数组长度，则第k个数为另外一个数组第k个数
        if a_begin>=len(a):
            return b[b_begin+k-1]*1.0
        if b_begin>=len(b):
            return a[a_begin+k-1]*1.0
        #k为1时，两数组最小的那个为第一个数
        if k==1:
            return min(a[a_begin],b[b_begin])*1.0
        #mid_a / mid_b 分别表示 a数组、b数组中第 k / 2 个数
        mid_a=1000000
        mid_b=1000000
        if (a_begin+k//2-1<len(a)):
            mid_a=a[a_begin+k//2-1]
        if (b_begin+k//2-1<len(b)):
            mid_b=b[b_begin+k//2-1]
        '''
        //如果a数组的第 k / 2 个数小于b数组的第 k / 2 个数，表示总的第 k 个数位于 a的第k / 2个数的后半段，或者是b的第 k / 2个数#的前半段
        //由于范围缩小了 k / 2 个数，此时总的第 k 个数实际上等于新的范围内的第 k - k / 2个数，依次递归
        '''
        if mid_a<mid_b:
            return self.find_kth(a,a_begin+k//2,b,b_begin,k-k//2)
        else:
            return self.find_kth(a,a_begin,b,b_begin+k//2,k-k//2)