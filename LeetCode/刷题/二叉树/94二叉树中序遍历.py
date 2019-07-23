'''
非递归
链接：https://leetcode-cn.com/problems/two-sum/solution/die-dai-he-di-gui-by-powcai/
'''
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        # 用p当做指针
        p = root
        while p or stack:
            # 把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            # 输出 栈顶元素
            tmp = stack.pop()
            res.append(tmp.val)
            # 看右子树
            p = tmp.right
        return res
#前序
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
#后续
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left :
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]