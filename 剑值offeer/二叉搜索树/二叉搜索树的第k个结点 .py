''''
给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
如果使用终须遍历，则得到的序列式为{2,3,4,5,6,7,8}。因此，只需要用中序遍历一棵二叉搜索树，就很容易找出它的第k大结点。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot==None or k==0:
            return  
        self.seq=[]
        self.middle(pRoot)
        if len(self.seq)<k:
            return
        return self.seq[k-1]
    
    def middle(self,root):
        if root==None:
            return 
        self.middle(root.left)
        self.seq.append(root)
        self.middle(root.right)

'''
别人的
'''
class Solution1:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        #第三个节点是4
        #前序遍历5324768
        #中序遍历2345678
        #后序遍历2436875
        #所以是中序遍历，左根右
        global result
        result=[]
        self.midnode(pRoot)
        if  k<=0 or len(result)<k:
            return None
        else:
            return result[k-1]
              
    def midnode(self,root):
        if not root:
            return None
        self.midnode(root.left)
        result.append(root)
        self.midnode(root.right)

class Solution2:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        global result 
        result = []
        def MSearch(node):
            if node is None:
                return
            else:
                MSearch(node.left)
                result.append(node)
                MSearch(node.right)
        MSearch(pRoot)
        if k > len(result) or k <= 0:
            return None
        else:
            return result[k - 1]

class Solution3(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res=[]
        def inorderTraversal(root):
            if not root:
                return []
            st=[(root,False)]
            while st:
                cur,vis=st.pop()
                if vis:
                    res.append(cur.val)
                else:
                    if cur.right:
                        st.append((cur.right,False))
                    st.append((cur,True))
                    if cur.left:
                        st.append((cur.left,False))
        inorderTraversal(root)
        if k>len(res) or k<=0:
            return None
        else:
            return res[k-1]