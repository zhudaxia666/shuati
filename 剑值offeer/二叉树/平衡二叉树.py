'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
平衡二叉树：是一种特殊的二叉排序树，它或者为空树，或者每个结点的左右子树都是平衡二叉树，也就是每个结点的左右子树的高度之差只能是-1,0,1三种情况。
思路：
用后序遍历的方式遍历二叉树的每一个结点，在遍历到一个结点之前我们就已经遍历了它的左右子树。
只要在遍历每个结点的时候记录它的深度（某一结点的深度等于它到叶结点的路径的长度），我们就可以一边遍历一边判断每个结点是不是平衡的。
'''
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.Treedepth(pRoot.left)-self.Treedepth(pRoot.right))>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def Treedepth(self,pRoot):
        if not pRoot:
            return 0
        left=self.Treedepth(pRoot.left)
        right=self.Treedepth(pRoot.right)
        return max(left,right)+1
'''
方法2
求树的深度是用了非递归！！！！！！！！！！！！！！！！
'''
class Solution:
     
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        return abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right))<=1
        # write code here
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        a = []
        a.insert(0, pRoot)
        n = 0
        while a:
            n += 1
            t = len(a)
            for i in range(t):
                temp = a.pop()
                if temp.left:
                    a.insert(0, temp.left)
                if temp.right:
                    a.insert(0, temp.right)
        return n