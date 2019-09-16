'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


思路1：将中序输出改成比较
'''
def isValidBST(root):
        if not root:
            return True
        stack=[]
        pre=-float('inf')
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                if root.val>pre:
                    pre=root.val
                    root=root.right
                else:
                    return False
        return True
'''
思路2：

'''