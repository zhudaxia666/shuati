'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k<1:
            return []
        stack=[]
        for i in range(len(nums)-k+1):
            m=max(nums[i:i+k])
            stack.append(m)
        return stack

'''
使用双向队列：
窗口的滑动过程中数字的进出类似一个队列中元素的出队入队，这里我们采用一个队列queue存储可能成为最大值的元素下标
(之所以队列中存元素下标而不是元素值本身，是因为队列并不存储所有元素，而我们需要知道什么时候队首元素已经离开滑动窗口)。
当遇到一个新数时，将它与队尾元素比较，如果大于队尾元素，则丢掉队尾元素，继续重复比较，直到新数小于队尾元素，或者队列为空为止，
将新数下标放入队列。同时需要根据滑动窗口的移动判断队首元素是否已经离开。

'''
def maxSlidingWindow1(nums,k):
    if not nums or k<1 or len(nums)<k:
        return []
    res=[]
    queue=[]
    for i in range(len(nums)):
        if len(queue)>0 and i-k>=queue[0]:
            queue.pop(0)
        while len(queue)>0 and nums[queue[-1]]<nums[i]:
            queue.pop()
        queue.append(i)
        if i>=k-1:
            res.append(nums[queue[0]])
    return res
    