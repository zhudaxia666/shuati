'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。

思路：
删除重复结点，只需要记录当前结点前的最晚访问过的不重复结点pPre、当前结点pCur、指向当前结点后面的结点pNext的三个指针即可。
如果当前节点和它后面的几个结点数值相同，那么这些结点都要被剔除，然后更新pPre和pCur；如果不相同，则直接更新pPre和pCur。

需要考虑的是，如果第一个结点是重复结点我们该怎么办？这里我们分别处理一下就好，
如果第一个结点是重复结点，那么就把头指针pHead也更新一下。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        pbef=None
        pcur=pHead
        pnext=None
        while pcur:
            if pcur.next!=None and pcur.next.val==pcur.val:
                pnext=pcur.next
                while pnext.next!=None and pnext.next.val==pcur.val:
                    pnext=pnext.next
                if pcur==pHead:
                    pHead=pnext.next
                else:
                    pbef.next=pnext.next
                pcur=pnext.next
            else:
                pbef=pcur
                pcur=pcur.next
        return pHead

'''
别人的
'''
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        result=ListNode(0)
        res=result
        result.next=pHead
        tmp=pHead
        while tmp and tmp.next:
            if tmp.val==tmp.next.val:
                while tmp.next and tmp.val==tmp.next.val:
                    tmp=tmp.next
            else:
                res.next=tmp
                res=res.next
            tmp=tmp.next
        res.next=tmp
        return result.next