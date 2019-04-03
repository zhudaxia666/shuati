'''
输入一个链表，输出该链表倒数第k个节点
思路

我们可以定义两个指针。第一个指针从链表的头指针开始遍历向前走k-1，第二个指针保持不动；
从第k步开始，第二个指针也开始从链表的头指针开始遍历。由于两个指针的距离保持在k-1，
当第一个（走在前面的）指针到达链表的尾结点时，第二个指针（走在后面的）指针正好是倒数第k个结点。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head==None or k==0:
            return None
        r=head
        l=head
        for i in range(k-1):
            if r.next==None:
                return None
            else:
                r=r.next
        while r.next:
            r=r.next
            l=l.next
        return l

'''

'''