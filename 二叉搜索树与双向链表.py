'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向

'''
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left=pRootOfTree.left
 # 连接根与左子树最大结点
        if left:
            while(left.right):
                left=left.right
            pRootOfTree.left,left.right=left,pRootOfTree
 # 处理右子树
        self.Convert(pRootOfTree.right)
        right=pRootOfTree.right
# 连接根与右子树最小结点
        if right:
            while(right.left):
                right=right.left
            pRootOfTree.right,right.left=right,pRootOfTree
             
        while(pRootOfTree.left):
            pRootOfTree=pRootOfTree.left
        return pRootOfTree

'''
下面的思路好容易理解
首先要知道二叉搜索树的中序遍历序列就是排序的数列,之后只需要把当前节点的右子树设为下一个节点,下一个节点的左子树设为该节点.
'''
class Solution1:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.mid = []
        self.middle(pRootOfTree)
        for i in range(len(self.mid)-1):
            self.mid[i].right = self.mid[i+1]
            self.mid[i+1].left = self.mid[i]

        return self.mid[0]

    def middle(self, root):
        if not root:
            return
        self.middle(root.left)
        self.mid.append(root)
        self.middle(root.right)