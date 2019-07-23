'''
给定一个二叉树，返回它的 前序 遍历。(通过迭代算法完成)
思路：
有两种通用的遍历树的策略：
深度优先搜索（DFS）
    在这个策略中，我们采用深度作为优先级，以便从跟开始一直到达某个确定的叶子，然后再返回根到达另一个分支。
    深度优先搜索策略又可以根据根节点、左孩子和右孩子的相对顺序被细分为前序遍历，中序遍历和后序遍历。
宽度优先搜索（BFS）
    我们按照高度顺序一层一层的访问整棵树，高层次的节点将会比低层次的节点先被访问到。

从根节点开始，每次迭代弹出当前栈顶元素，并将其孩子节点压入栈中，先压右孩子再压左孩子。
在这个算法中，输出到最终结果的顺序按照 Top->Bottom 和 Left->Right，符合前序遍历的顺序。

算法复杂度
时间复杂度：访问每个节点恰好一次，时间复杂度为 O(N)O(N) ，其中 NN 是节点的个数，也就是树的大小。
空间复杂度：取决于树的结构，最坏情况存储整棵树，因此空间复杂度是 O(N)。
'''
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self,root):
        if not root: 
            return []
        stack=[root]
        res=[]
        while stack:
            node=stack.pop()
            if node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res
             
