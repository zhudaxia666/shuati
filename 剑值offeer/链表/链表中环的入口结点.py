'''
一个链表中包含环，请找出该链表的环的入口结点
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return None
        dict1=[]
        dict1.append(pHead)
        t=pHead.next
        while t:
            if t in dict1:
                return t
            dict1.append(t)
            t=t.next
        return None

"""
别人的
"""
class Solution1:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        plist = []
         
        while True:
            plist.append(pHead)
            pHead = pHead.next
            if not pHead:
                return None
            if pHead in plist:
                return pHead

'''
第一步，找环中相汇点。分别用p1，p2指向链表头部，p1每次走一步，p2每次走二步，直到p1==p2找到在环中的相汇点。
第二步，找环的入口。接上步，当p1==p2时，p2所经过节点数为2x,p1所经过节点数为x,设环中有n个节点,p2比p1多走一圈有2x=n+x; n=x;
可以看出p1实际走了一个环的步数，再让p2指向链表头部，p1位置不变，p1,p2每次走一步直到p1==p2; 此时p1指向环的入口。
'''
class Solution3:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return None
        p1=pHead
        p2=pHead
        while p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                p2=pHead
                while p1!=p2:
                    p1=p1.next
                    p2=p2.next
                if p1==p2:
                    return p1
        return None

'''
可以用两个指针来解决这个问题。先定义两个指针P1和P2指向链表的头结点。如果链表中的环有n个结点，指针P1先在链表上向前移动n步，
然后两个指针以相同的速度向前移动。当第二个指针指向的入口结点时，第一个指针已经围绕着揍了一圈又回到了入口结点。
现在，关键问题在于怎么知道环中有几个结点呢？
可以使用快慢指针，一个每次走一步，一个每次走两步。如果两个指针相遇，表明链表中存在环，并且两个指针相遇的结点一定在环中。
随后，我们就从相遇的这个环中结点出发，一边继续向前移动一边计数，当再次回到这个结点时，就可以得到环中结点数目了。
'''
class Solution2:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None:
            return None
        meetingnode = self.MeetingNode(pHead)
        if meetingnode == None:
            return None
        nodeslop = 1
        node1 = meetingnode
        while node1.next != meetingnode:
            node1 = node1.next
            nodeslop += 1
        node1 = pHead
        for _ in range(nodeslop):
            node1 = node1.next
        node2 = pHead
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next
        return node1
        
    def MeetingNode(self, pHead):
        slow = pHead.next
        if slow == None:
            return None
        fast = slow.next
        while fast != None and slow != None:
            if slow == fast:
                return fast
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
        return None