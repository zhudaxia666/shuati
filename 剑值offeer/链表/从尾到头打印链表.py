'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
自己写的
'''
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        re_list=[]
        if listNode==None:
            return re_list
        head=listNode
        while head:
            re_list.append(head.val)
            head=head.next
        n=len(re_list)
        for i in range(n//2):
            re_list[i],re_list[n-1-i]=re_list[n-1-i],re_list[i]
        return re_list
'''
别人的
'''
class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

    
def printListFromTailToHead(self, listNode):
        # write code here
        l = list()
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]

#deque模块是python标准库collections中的一项，它提供了两端都可以操作的序列，这意味着，在序列的前后你都可以执行添加或删除操作。
from collections import deque
class Solution1:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        temp = deque()
        while listNode:
            temp.appendleft(listNode.val)
            listNode = listNode.next
        return temp



