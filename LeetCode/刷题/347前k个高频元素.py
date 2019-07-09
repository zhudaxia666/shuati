'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。



'''
def topKFrequent(nums, k):
        d = {}
        res = []
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        d_by_value = sorted(d.items(),key=lambda d: d[1],reverse=True)
        print(d_by_value)
        for i in range(k):
            res.append(d_by_value[i][0])
        return res
topKFrequent([1,1,1,2,2,3],2)

class Solution1:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """   
        import heapq
        count_list = dict()
        for i in nums:
            count_list[i] = count_list.get(i, 0) + 1

        p = list()
        for i in count_list.items():
            if len(p) == k:
                if i[1] > p[0][0]:
                    heapq.heappop(p)
                    heapq.heappush(p, (i[1], i[0]))
            else:
                heapq.heappush(p, (i[1], i[0]))

        return [i[1] for i in p]

'''
第一步：hash统计次数（在Python中要巧用字典） 第二步：字典键值对压入大顶堆（注意如何将heapq小顶堆作为大顶堆使用）
第三步：大顶堆吐出k个值加入返回list
'''

import heapq
class Solution2:
    def topKFrequent(self, nums, k):
        heap_max = []
        dic_fre = {}
        ans = []
        for i in nums:
            if i in dic_fre:
                dic_fre[i]+=1
            else:
                dic_fre[i] = 1
        for i in dic_fre:
            heapq.heappush(heap_max,(-dic_fre[i],i))
        for j in range(k):
            p = heapq.heappop(heap_max)
            ans.append(p[1])
        return ans