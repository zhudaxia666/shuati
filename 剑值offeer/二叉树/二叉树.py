class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
class Tree:
    def __init__(self):
        self.root=Node()
    def preTraverse(self,root):
        '''
        前序遍历
        '''
        if root==None:
            return
        print(root.value)
        self.preTraverse(root.left)
        self.preTraverse(root.right)
    def midTraverse(self,root):
        '''
        中序遍历
        '''
        if root==None:
            return
        self.midTraverse(root.left)
        print(root.value)
        self.midTraverse(root.right)
    def afterTraverse(self,root):
        '''
        后序遍历
        '''
        if root==None:
            return
        self.afterTraverse(root.left)
        self.afterTraverse(root.right)
        print(root.value)
'''
那么，如果我们已知二叉树的前序遍历和中序遍历，求这棵二叉树的后序遍历
'''
preList = list('12473568')
midList = list('47215386')
afterList = []

def findTree(preList, midList, afterList):
    if len(preList) == 0:
        return
    if len(preList) == 1:
        afterList.append(preList[0])
        return
    root = preList[0]
    n = midList.index(root)
    findTree(preList[1:n + 1], midList[:n], afterList)
    findTree(preList[n + 1:], midList[n + 1:], afterList)
    afterList.append(root)

if __name__ == "__main__":
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    # root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    tree=Tree()
    print('前序遍历：')
    tree.preTraverse(root)
    print('中序遍历：')
    tree.midTraverse(root)
    print('后序遍历：')
    tree.afterTraverse(root)
    