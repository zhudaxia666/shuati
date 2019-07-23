'''
给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
以 10^9 + 7 为模，返回这些数字之和。
输入：[1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
'''
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mod = 10 ** 9 + 7
        self.ans = 0
        def dfs(root, now):
            if root == None:
                return
            if root.left == root.right == None:
                self.ans = (self.ans + now * 2 + root.val) % mod
                return
            dfs(root.left, (now * 2 + root.val) % mod)
            dfs(root.right, (now * 2 + root.val) % mod)
        dfs(root, 0)
        return self.ans
