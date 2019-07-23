'''
给定一个二叉树，在树的最后一行找到最左边的值
思路：
层次遍历,不过是从右到左遍历。建立一个栈保存层次遍历的结点，则最后一个节点就是最后一行最左边的节点
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack=[]
        stack.append(root)
        node=None
        while stack:
            node=stack.pop(0)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return node.val