class Treenode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class zaozuo():
    def insert(self,root,data):
        '''二叉搜索树插入操作'''
        if root ==None:
            root=Treenode(data)
        elif data<root.val:
            self.insert(root.left,data)
        elif data>root.val:
            self.insert(root.right,data)
        return root
    '''
    从根节点开始查找，待查找的值是否与根节点的值相同，若相同则返回True；否则，判断待寻找的值是否比根节点的值小，
    若是则进入根节点左子树进行查找，否则进入右子树进行查找。该操作使用递归实现
    '''
    def query(self,root,data):
        if root==None:
            return False
        elif root.val==data:
            return True
        elif root.val>data:
            return self.query(root.left,data)
        else:
            return self.query(root.right,data)
        '''
        查找最小值：从根节点开始，沿着左子树一直往下，直到找到最后一个左子树节点，按照定义可知，
        该节点一定是该二叉搜索树中的最小值节点。
        '''
    def findmin(self,root):
        if root.left:
            return self.findmin(root.left)#查找最大值就遍历root.right
        else:
            return root
    '''
    对二叉搜索树节点的删除操作分为以下三种情况：
  （1）待删除节点既无左子树也无右子树：直接删除该节点即可
  （2）待删除节点只有左子树或者只有右子树：将其左子树或右子树根节点代替待删除节点
  （3）待删除节点既有左子树也有右子树：找到该节点右子树中最小值节点，使用该节点代替待删除节点，然后在右子树中删除最小值节点。
    '''
    def delnode(self,root,data):
        if root==None:
            return 
        if data<root.val:
            root.left=self.delnode(root.left,data)
        elif data>root.val:
            root.right=self.delnode(root.right,data)
         # 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
        else:
            if root.left and root.right:
                # 既有左子树又有右子树，则需找到右子树中最小值节点
                tem=self.findmin(root.right)
                root.val=tem.val
                # 再把右子树中最小值节点删除
                root.right=self.delnode(root.right,tem.val)
            elif root.left==None and root.right==None:
                # 左右子树都为空
                root=None
            elif root.left==None:
                # 只有右子树
                root=root.right
            elif root.right==None:
                # 只有左子树
                root=root.left
        return root
    '''
     实现二叉搜索树的中序遍历，并打印出来。该方法打印出来的数列将是按照递增顺序排列。
    '''
    def printTree(self,root):
        # 打印二叉搜索树(中序打印，有序数列)
        if root == None:
            return 
        self.printTree(root.left)
        print(root.val, end = ' ')
        self.printTree(root.right)
# class TreeNode:
# 	def __init__(self,val):
# 		self.val=val
# 		self.left=None
# 		self.right=None
# def insert(root,val):
# 	if root is None:
# 		root=TreeNode(val)
# 	else:
# 		if val<root.val:
# 			root.left=insert(root.left,val)   #递归地插入元素
# 		elif val>root.val:
# 			root.right=insert(root.right,val)  
# 	return root

# def query(root,val):
# 	if root is None:
# 		return 
# 	if root.val is val:
# 		return 1
# 	if root.val <val:
# 		return query(root.right,val)  #递归地查询
# 	else:  
# 		return query(root.left,val)
# def findmin(root):
# 	if root.left:
# 		return findmin(root.left)
# 	else:
# 		return root
	
# def delnum(root,val):
# 	if root is None:
# 		return 
# 	if val<root.val:
# 		return delnum(root.left,val)
# 	elif val>root.val:
# 		return delnum(root.right,val)
# 	else:                                             # 删除要区分左右孩子是否为空的情况
# 		if(root.left and root.right):
			
# 			tmp=finmin(root.right)             #找到后继结点
# 			root.val=tmp.val
# 			root.right=delnum(root.right,val)    #实际删除的是这个后继结点
			
# 		else:
# 			if root.left is None:
# 				root=root.right
# 			elif root.right is None:
# 				root=root.left
# 	return root
# def printTree(root):
#     # 打印二叉搜索树(中序打印，有序数列)
#     if root == None:
#         return 
#     printTree(root.left)
#     print(root.val, end = ' ')
#     printTree(root.right)

if __name__ == "__main__":
    root=Treenode(3)
    a=zaozuo()
    root=a.insert(root,1)
    root=a.insert(root,2)
    root=a.insert(root,5)
    a.printTree(root)
    


    # root=TreeNode(3)
    # root=insert(root,2)
    # root=insert(root,1)
    # root=insert(root,4)
    # printTree(root)

    # print (query(root,3))
    # print (query(root,1))
    # root=delnum(root,1)
    # print (query(root,1))

    
