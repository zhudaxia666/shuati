'''
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = []
        if not root.left and not root.right:
            return root.val
        else:
            self.findPath(root.left, [root.val], result)
            self.findPath(root.right, [root.val], result)
        return sum(result)
    def findPath(self, node, temp_path, result):
        if not node:
            return
        temp_path.append(node.val)
        if not node.left and not node.right:
            path_sum = 0
            for value in temp_path:
                path_sum *= 10
                path_sum += value                
            result.append(path_sum)
        else:
            self.findPath(node.left, temp_path, result)
            self.findPath(node.right, temp_path, result)
        temp_path.pop()        
        return
def sumNumbers(self, root):
    if root==None:
        return 0
    return self.sumNumber(root,0)
    def sumNumber(self,root,t):
        l=0
        r=0
        if root.left==None and root.right==None:
            return t+root.val
        if root.left!=None:
            l=self.sumNumber(root.left,10*(t+root.val))
        if root.right!=None:
            r=self.sumNumber(root.right,10*(t+root.val))
        return l+r
'''
给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
以 10^9 + 7 为模，返回这些数字之和。
输入：[1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
'''
class Solution2(object):
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
'''
返回从根到叶子节点的所有路径
'''
import copy
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
def dfs(node, result, tmp=list()):
    if node is None:
        return
    tmp.append(node)
    # 这里需要用拷贝而不是用 = 赋值，也可以遍历赋值
    tmp1 = copy.deepcopy(tmp)
    if node.left is None and node.right is None:
        result.append([i.val for i in tmp])
        return
    if node.left is not None:
        dfs(node.left, result, tmp)
    # 遍历右子树需要带上不同的变量，否则左子树的tmp和右子树的tmp都指向一块内存
    if node.right is not None:
        dfs(node.right, result, tmp1)


if __name__ == '__main__':
    node1 = TreeNode('a')
    node2 = TreeNode('b')
    node3 = TreeNode('c')
    node4 = TreeNode('d')
    node5 = TreeNode('e')
    node6 = TreeNode('f')
    node7 = TreeNode('g')

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node4.left = node6
    node3.left = node7

    r = []
    dfs(node1, result=r)
    print(r)