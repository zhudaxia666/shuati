'''
给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。
返回移除了所有不包含 1 的子树的原二叉树。
( 节点 X 的子树为 X 本身，以及所有 X 的后代。)
示例1:
输入: [1,null,0,0,1]
输出: [1,null,0,null,1]

思路：
左右根遍历，保证了删空子树时，如果根节点也是0，那就继续删除根节点
'''

class Solution:
    def pruneTree(self,root):
        if not root:
            return None
        root.left=self.pruneTree(root.left)
        root.right-self.pruneTree(root.right)
        if root.val==0 and not root.left and not root.right:
            return None
        else:
            return root

