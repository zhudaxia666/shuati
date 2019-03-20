'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
'''
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         start,move=0,0
#         l=head
#         r=head
#         i=0
#         while r:
#             i+=1
#             r=r.next
#         if i==n:
#             head=head.next
#             return head
#         else:
#             r=head
#             while r:
#                 r=r.next
#                 move+=1
#                 if (move-start)==n:
#                     break
#             while r.next:
#                 l=l.next
#                 r=r.next
#             l.next=l.next.next
#             return head

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = pre = head
        
        for i in range(n):
            cur = cur.next#前指针先走n步，然后后指针再走
        if cur == None:#若走n步为空就是删除头结点
            return head.next
        while cur != None:   
            if cur.next == None and n == 1:    #这是针对两个节点
                pre.next = None
                return head
            pre = pre.next
            cur = cur.next
            
        pre.val = pre.next.val
        pre.next = pre.next.next
        return head