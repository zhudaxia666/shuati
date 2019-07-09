'''
编写一个程序，找到两个单链表相交的起始节点。

思路：
链表1的长度是x1+y，链表2的长度是x2+y，我们同时遍历链表1和链表2，到达末尾时，再指向另一个链表。则当两链表走到相等的位置时：
x1+y+x2 = x2+y+x1
没交点则y=0, 结尾都指向None。
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha