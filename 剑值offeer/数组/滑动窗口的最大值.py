'''
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}，
 {2,3,4,2,6,[2,5,1]}。
'''
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        if len(num)<size or not num or not size:
            return []
        max_val=[]
        for i in range(len(num)-size+1):
            max_val.append(max(list(num[i:size])))
            size+=1
        return max_val

'''

'''
# -*- coding:utf-8 -*-
class Solution1:
    def maxInWindows(self, num, size):
        queue,res,i = [],[],0
        while size>0 and i<len(num):
            if len(queue)>0 and i-size+1 > queue[0]: #若最大值queue[0]位置过期 则弹出 
                queue.pop(0)
            while len(queue)>0 and num[queue[-1]]<num[i]: #每次弹出所有比num[i]小的数字
                queue.pop()
            queue.append(i)
            if i>=size-1:
                res.append(num[queue[0]])
            i += 1
        return res

'''
借助一个辅助队列，从头遍历数组，根据如下规则进行入队列或出队列操作： 
0. 如果队列为空，则当前数字入队列 
1. 如果当前数字大于队列尾，则删除队列尾，直到当前数字小于等于队列尾，或者队列空，然后当前数字入队列 
2. 如果当前数字小于队列尾，则当前数字入队列 
3. 如果队列头超出滑动窗口范围，则删除队列头 
这样能始终保证队列头为当前的最大值

原文：https://blog.csdn.net/u010429424/article/details/73692248 
'''
class Solution3:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size<1 or len(num)<size:
            return []
        res=[]
        queue=[]
        for i in range(len(num)):
            if len(queue)>0 and i-size>=queue[0]:#// 如果队列头元素不在滑动窗口中了，就删除头元素
                queue.pop(0)
            #// 如果当前数字大于队列尾，则删除队列尾，直到当前数字小于等于队列尾，或者队列空
            while len(queue)>0 and num[queue[-1]]<num[i]:
                queue.pop()
            queue.append(i)#入队列
            # // 滑动窗口经过size个元素，获取当前的最大值，也就是队列的头元素
            if i>=size-1:
                res.append(num[queue[0]])
        return res
                