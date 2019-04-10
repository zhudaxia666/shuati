'''
该模块提供了堆排序算法的实现。堆是二叉树，最大堆中父节点大于或等于两个子节点，最小堆父节点小于或等于两个子节点
heapq有两种方式创建堆， 一种是使用一个空列表，
然后使用heapq.heappush()函数把值加入堆中，另外一种就是使用heap.heapify(list)转换列表成为堆结构
'''
import heapq
# 第一种
"""
函数定义：
heapq.heappush(heap, item)
    - Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap)
    - Pop and return the smallest item from the heap, maintaining the heap invariant.
    If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
"""
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)  # 加入堆
print(heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果

# 第二种
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)
print([heapq.heappop(nums) for _ in range(len(nums))])  # 堆排序结果

"""
heapq 模块还有一个heapq.merge(*iterables) 方法，用于合并多个排序后的序列成一个排序后的序列， 返回排序后的值的迭代器。
类似于sorted(itertools.chain(*iterables))，但返回的是可迭代的
函数定义：
heapq.merge(*iterables)
    - Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.
    - Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once, and assumes that each of the input streams is already sorted (smallest to largest).
"""
import heapq

num1 = [32, 3, 5, 34, 54, 23, 132]
num2 = [23, 2, 12, 656, 324, 23, 54]
num1 = sorted(num1)
num2 = sorted(num2)

res = heapq.merge(num1, num2)
print(list(res))

#如果需要删除堆中最小元素并加入一个元素，可以使用heapq.heaprepalce() 函数
import heapq
nums = [1, 2, 4, 5, 3]
heapq.heapify(nums)
heapq.heapreplace(nums, 23)
print([heapq.heappop(nums) for _ in range(len(nums))])


#如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数
"""
函数定义：
heapq.nlargest(n, iterable[, key])¶
    - Return a list with the n largest elements from the dataset defined by iterable. 
    - key if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.lower
    - Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
"""
import heapq

nums = [1, 3, 4, 5, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

"""
输出：
[5, 4, 3]
[1, 2, 3]
"""
