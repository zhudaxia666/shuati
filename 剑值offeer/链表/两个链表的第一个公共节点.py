'''
输入两个链表，找出它们的第一个公共结点。
思路：
首先遍历两个链表得到他们的长度，就能知道哪个链表比较长，以及长几个节点。在第二次遍历的时候在最长的链表上先走几步，接着
同时在链表上遍历
'''
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        p=pHead1
        q=pHead2
        c1=0
        c2=0
        while p:
            c1+=1
            p=p.next
        while q:
            c2+=1
            q=q.next
        p=pHead1
        q=pHead2
        if c1>=c2:
            p=self.pre(c1-c2,p)
        else:
            q=self.pre(c2-c1,q)
        while p and q:
            if p==q:
                return p
            p=p.next
            q=q.next
        return None
    def pre(self,num,node):
        while num>0:
            node=node.next
            num-=1
        return node

def FindFirstCommonNode2(self, head1, head2):
        if not head1 or not head2:
            return None
        p1, p2= head1, head2
        length1 = length2 = 0
        while p1:
            length1 += 1
            p1 = p1.next
        while p2:
            length2 += 1
            p2 = p2.next
        if length1 > length2:
            while length1 - length2:
                head1 = head1.next
                length1 -= 1
        else:
            while length2 - length1:
                head2 = head2.next
                length2 -= 1
        while head1 and head2:
            if head1 is head2:
                return head1
            head1 = head1.next
            head2 = head2.next
        return None
            