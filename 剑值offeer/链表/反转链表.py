'''
输入一个链表。反转链表后，输出链表的所有元素
思路：
使用三个指针，分别指向当前遍历到的结点，它的前一个结点以及后一个结点
在遍历的时候，做当前结点的下一个结点指向前一个结点
'''
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead==None or pHead.next==None:
            return pHead
        last=None
        while pHead:
            tem=pHead.next
            pHead.next=last
            last=pHead
            pHead=tem
        return last
