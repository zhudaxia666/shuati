'''
统计一个数字在排序数组中出现的次数
'''
#方法1
# -*- coding:utf-8 -*-
class Solution1:
    def GetNumberOfK(self, data, k):
        # write code here
        count = len(data)
        i = 0
        for j in range(count):
            if data[j] == k:
                i += 1
        return i
 
#方法2
# -*- coding:utf-8 -*-
class Solution3:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data)==0 or k not in data:
            return 0
        else:
            return data.count(k)

#方法3：
# -*- coding:utf-8 -*-
'''
既然是已经排序好的数组，那么第一个想到的就是二分查找法。
做法就是使用二分法找到数字在数组中出现的第一个位置，再利用二分法找到数字在数组中出现的第二个位置。
时间复杂度为O(nlogn + nlogn)，最终的时间复杂度为O(nlogn)。
举个例子，找到数字k在数组data中出现的次数。
数组data中，数字k出现的第一个位置：
我们对数组data进行二分，如果数组中间的数字小于k，说明k应该出现在中间位置的右边；如果数组中间的数字大于k，
说明k应该出现在中间位置的左边；如果数组中间的数字等于k，并且中间位置的前一个数字不等于k，说明这个中间数字就是数字k出现的第一个位置。
同理，数字k出现的最后一个位置，也是这样找的。但是判断少有不同。我们使用两个函数分别获得他们。
'''
class Solution2:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        if len(data) == 1 and data[0] != k:
            return 0
        left = 0
        right = len(data) - 1
        first_k = 0
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:
                if mid == 0:
                    first_k = 0
                    break
                elif data[mid-1] != k:
                    first_k = mid
                    break
                else:
                    right = mid - 1       
        left = 0
        right = len(data) - 1
        last_k = -1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:               
                if mid == len(data) - 1:
                    last_k = len(data) - 1
                    break
                elif data[mid+1] != k:
                    last_k = mid
                    break
                else:
                    left = mid + 1       
        return last_k - first_k + 1
