'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

利用快速排序思想，对数组进行划分，并且判断划分的边界元素位置mid是否为第k大的数(k - 1)； 
若是则返回该数，若mid > k - 1说明第k大的数在左半边数组里；若mid < k - 1说明在右半边数组里。
对其继续进行数组划分，直到找到第k大的数。 数组划分函数partation采用数组中心位置的元素值作为bound（边界），
 也可以采用随机元素，最好不要用第一个（最后一个）元素，防止数组绝大部分元素是有序的，影响查找效率。

作者：liushang-leecode
链接：https://leetcode-cn.com/problems/two-sum/solution/kuai-su-pai-xu-si-xiang-shu-zu-hua-fen-by-liushang/

'''
class Solution:
   def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quicksort(nums,left,right,k):
            if left>right:
                return -1
            # /按照基准值将待排序区间划分为两个子区间
            div=partsort(nums,left,right)
            if div==k-1:
                return nums[div]
            elif div<k-1:
                return quicksort(nums,div+1,right,k)
            else:
                return quicksort(nums,left,div-1,k)
            #子问题排序左子树
            quicksort(nums,left,div-1,k)
            #子问题排序右子树
            quicksort(nums,div+1,right,k)
            return -1
        def partsort(nums,begin,end):
            #从大到小排序
            key=nums[end]
            last=end
            while begin<end:
                #左边找到小于基准值的元素
                while begin<end and nums[begin]>=key:
                    begin+=1
                 #右边找到大于基准值的元素
                while begin<end and nums[end]<=key:
                    end-=1
                #交换两个值
                nums[begin],nums[end]=nums[end],nums[begin]
            #两个下标走到一块的时候，把基准值交换过来
            nums[begin],nums[last]=nums[last],nums[begin]
            return begin
        return quicksort(nums,0,len(nums)-1,k)

#最小堆
class Solution1(object):
    def findKthLargest(self, array, k):
        def heap_build(parent,heap):
            child = 2*parent+1
            while child<len(heap):
                if child+1<len(heap) and heap[child+1]<heap[child]:
                    child = child+1
                if heap[parent]<= heap[child]:
                    break
                heap[parent],heap[child] = heap[child],heap[parent]
                parent,child = child,2*child+1
            return heap
        if k > len(array):
            return None
        heap = array[:k]
        for i in range(k,-1,-1):
            heap_build(i,heap)
        for j in range(k,len(array)):
            if array[j]>heap[0]:
                heap[0] = array[j]
                heap_build(0,heap)
        return heap[0]


           

