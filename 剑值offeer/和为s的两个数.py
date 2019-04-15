'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array)<2:
            return []
        if len(array)>0 and tsum<array[0]:
            return []
        m=float("inf")
        i=0
        flag=0
        while i<(len(array)-1):
            target=tsum-array[i]
            if target in array[i+1:]:
                flag=1
                array.remove(target)
                if target*array[i]<m:
                    m=target*array[i]
                    index=i
            i+=1
        if flag==1:
            return array[index],tsum-array[index]
        else:
            return []


'''
别人的思路：
对于一个数组，我们可以定义两个指针，一个从左往右遍历（pleft），另一个从右往左遍历（pright）。
首先，我们比较第一个数字和最后一个数字的和curSum与给定数字sum，如果curSum < sum，那么我们就要加大输入值，
所以，pleft向右移动一位，重复之前的计算；如果curSum > sum，那么我们就要减小输入值，所以，pright向左移动一位，重复之前的计算；如果相等，那么这两个数字就是我们要找的数字，直接输出即可。

这么做的好处是，也保证了乘积最小。
'''
# -*- coding:utf-8 -*-
class Solution1:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array)<2:
            return []
        if len(array)>0 and tsum<array[0]:
            return []
        left,right=0,len(array)-1
        while left<right:
            if array[left]+array[right]==tsum:
                return array[left],array[right]
            elif array[left]+array[right]<tsum:
                left+=1
            else:
                right-=1
        return []