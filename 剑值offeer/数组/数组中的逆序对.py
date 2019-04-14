#每次找到最小值，此时的逆序对是最小值的索引，然后删掉最小值，继续上一步
# def InversePairs(data):
#         if len(data)<=1:
#             return 0
#         num=0
#         while data:
#             if sorted(data)==data:
#                 break
#             min_index=data.index(min(data))
#             num+=min_index
#             data.pop(min_index)
#         return num
# l=[1,4,2,6,3,0]
# print(InversePairs(l))

# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
def InversePairs(data):
    # write code here
    if not data:
        return 0
    temp = [i for i in data]
    return mergeSort(temp, data, 0, len(data)-1) % 1000000007
    
def mergeSort(temp, data, low, high):
    if low >= high:
        temp[low] = data[low]
        return 0
    mid = (low + high) / 2
    left = mergeSort(data, temp, low, mid)
    right = mergeSort(data, temp, mid+1, high)
        
    count = 0
    i = low
    j = mid+1
    index = low
    while i <= mid and j <= high:
        if data[i] <= data[j]:
            temp[index] = data[i]
            i += 1
        else:
            temp[index] = data[j]
            count += mid-i+1
            j += 1
        index += 1
    while i <= mid:
        temp[index] = data[i]
        i += 1
        index += 1
    while j <= high:
        temp[index] = data[j]
        j += 1
        index += 1
    return count + left + right
l=[1,4,2,6,3,0]
# a=Solution()
print(InversePairs(l))

import time
import copy
class Solution1:
    def InversePairs(self, array):
        if not array:
            return 0
        arrCopy = copy.deepcopy(array)
        return self.InverseRecur(array, arrCopy, 0, len(array)-1)

    def InverseRecur(self, array, arrCopy, start, end):
        if start == end:
            return 0
        mid = (start + end) // 2
        left = self.InverseRecur(array, arrCopy, start, mid)
        right = self.InverseRecur(array, arrCopy, mid+1, end)
        count = 0
        i = mid
        j = end
        locCopy = end
        while i>=start and j > mid:
            if array[i] > array[j]:
                count += j - mid
                arrCopy[locCopy] = array[i]
                locCopy -= 1
                i -= 1
            else:
                arrCopy[locCopy] = array[i]
                locCopy -= 1
                i -= 1

        while i >= start:
            arrCopy[locCopy] = array[i]
            locCopy -= 1
            i -= 1
        while j > mid:
            arrCopy[locCopy] = array[j]
            locCopy -= 1
            j -= 1
        s = start
        while s <= end:
            array[s] = arrCopy[s]
            s += 1
        return left + right + count
