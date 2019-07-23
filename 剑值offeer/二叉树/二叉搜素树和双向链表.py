'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向

思路：
二叉树的中序遍历
中序遍历中每个节点的链接
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#非递归版
class Solution1:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        p=pRootOfTree
        stack=[]
        restack=[]
        #这个循环是中序遍历
        while p or stack:
            if p:
                stack.append(p)
                p=p.left
            else:
                node=stack.pop()
                restack.append(node)
                p=node.right
        p=restack[0]
        while restack:
            top=restack.pop(0)
            if restack:
                top.right=restack[0]
                restack[0].left=top
        return p
#递归版
class Solution2:
    def Convert(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
         
        # 将左子树构建成双链表，返回链表头
        left = self.Convert(root.left)
        p = left
         
        # 定位至左子树的最右的一个结点
        while left and p.right:
            p = p.right
         
        # 如果左子树不为空，将当前root加到左子树链表
        if left:
            p.right = root
            root.left = p
         
        # 将右子树构造成双链表，返回链表头
        right = self.Convert(root.right)
        # 如果右子树不为空，将该链表追加到root结点之后
        if right:
            right.left = root
            root.right = right
             
        return left if left else root
            