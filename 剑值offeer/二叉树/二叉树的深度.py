''''
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def __init__(self):
        self.dep=0
    def TreeDepth(self, pRoot):
        # write code here
        if  not pRoot:
            return 0
        if not pRoot.left and not pRoot.right:
            return 1
        self.dfs(pRoot,[])
        return self.dep
    def dfs(self,node,result):
        if not node:
            return
        result.append(node)
        res=copy.deepcopy(result)
        if node.left==node.right==None:
            if len(result)>self.dep:
                self.dep=len(result)
            return
        if node.left:
            self.dfs(node.left,result)
        if node.right:
            self.dfs(node.right,res)

#方法2
class Solution1:
    def TreeDepth(self, pRoot):
        # write code here
        if  not pRoot:
            return 0
        left=self.TreeDepth(pRoot.left)
        right=self.TreeDepth(pRoot.right)
        return max(left,right)+1        

#非递归方法：！！！！！！！！！！！！！！！！！！
class Solution3:
    def TreeDepth(self, pRoot):
        # write code here
        if  not pRoot:
            return 0
        a=[pRoot]
        d=0
        while a:
            b=[]
            for node in a:
                if node.left:
                    b.append(node.left)
                if node.right:
                    b.append(node.right)
            a=b
            d+=1
        return d