'''
请实现两个函数，分别用来序列化和反序列化二叉树
序列化二叉树：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串。需要注意的是，序列化二叉树的过程中，
如果遇到空节点，需要以某种符号（这里用#）表示。以下图二叉树为例，序列化二叉树时，需要将空节点也存入字符串中。
序列化可以基于先序/中序/后序/按层等遍历方式进行，这里采用先序遍历的方式实现，字符串之间用 “，”隔开

反序列化二叉树：根据某种遍历顺序得到的序列化字符串，重构二叉树。具体思路是按前序遍历“根左右”的顺序，
根节点位于其左右子节点的前面，即非空（#）的第一个节点是某子树的根节点，左右子节点在该根节点后，以空节点#为分隔符

'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution1:
    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val)+','+self.Serialize(root.left)+','+self.Serialize(root.right)
    def Deserialize(self, s):
        list1=s.split(',')
        return self.DeserializeTree(list1)
    def DeserializeTree(self,s):
        if not s:
            return None
        val=s.pop(0)
        root=None
        if val!='#':
            root=TreeNode(int(val))
            root.left=self.DeserializeTree(s)
            root.right=self.DeserializeTree(s)
        return root

'''
'''
class Solution2:
    flag = -1
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
     
    def Deserialize(self, s):
        # write code here
        self.flag += 1
         
        l = s.split(',')
        if self.flag >= len(s):
            return None
         
        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
