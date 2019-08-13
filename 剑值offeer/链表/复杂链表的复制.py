'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

思路：
 1. 把复制的结点链接在原始链表的每一对应结点后面 
 2. 把复制的结点的random指针指向被复制结点的random指针的下一个结点
 3. 拆分成两个链表，奇数位置为原链表，偶数位置为复制链表，注意复制链表的最后一个结点的next指针不能跟原链表指向同一个空结点None，
 next指针要重新赋值None(判定程序会认定你没有完成复制）
'''
# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        curhead=pHead
        while curhead:
            p=RandomListNode(curhead.label)
            q=curhead.next
            curhead.next=p
            p.next=q
            curhead=q
        curhead=pHead
        while curhead:
            p=curhead.next
            if curhead.random==None:
                p.random=None
            else:
                p.random=curhead.random.next
            curhead=p.next
        cur=pHead
        p=pHead.next
        while cur:
            q=cur.next
            tmp=q.next
            cur.next=tmp
            if tmp:
                q.next=tmp.next
            else:
                q.next=None
            cur=tmp
        return p