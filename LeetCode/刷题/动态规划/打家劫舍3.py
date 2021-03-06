'''
/*
//递归思想（不要深入递归函数体，只需知道递归函数的功能，以及找到跳出递归的边界条件）
        //思路：
        //能盗取的最高金额为 抢劫该节点+抢劫该节点的左孩子的左右子树+抢劫该节点的右孩子的左右子树
        //与 抢劫该节点的左子树+抢劫该节点的右子树的和  的最大值
        //执行用时 1005ms  原因是出现了很多重复的计算，可使用动态规划解决
        if(root == null) return 0;
        int val = 0;
        if(root.left != null) val += rob(root.left.left) + rob(root.left.right);
        if(root.right != null) val += rob(root.right.left) + rob(root.right.right);
        return Math.max(rob(root.left) + rob(root.right),val + root.val);
        */

//动态规划
        //思路：
        //定义一个数组res,长度为2,res[0]表示不抢该节点可获得最大值,res[1]表示抢劫该节点可获得最大值
        //方法helper(r)意为：在以r为根节点的树中,返回抢劫根节点与不抢劫根节点可获得的最大值
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        res=self.helper(root)
        return max(res)
    def helper(self,root):
        if not root:#边界条件，r为null时，跳出
            return [0,0]
        #对于以r.left为根的树，计算抢劫根节点(r.left)与不抢劫根节点可获得最大金额. 
        # left[0]则为不抢r.lrft可获得的最大金额,left[1]则为抢劫r.left可获得的最大金额  以下right[] 分析同理
        left=self.helper(root.left)
        right=self.helper(root.right)
        skip=max(left)+max(right)#计算不抢劫当前根节点可获得的最大金额(那么其左右子树可以随便抢)
        rob=root.val+left[0]+right[0]#计算若抢劫根节点可获得的最大金额(此时,其左右子树的根节点不能被抢)
        return [skip,rob]