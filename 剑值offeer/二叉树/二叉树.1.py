class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def preTraverse(root):
    '''
    前序遍历
    '''
    if root==None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)
def midTraverse(root):
    '''
    中序遍历
    '''
    if root==None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)
def afterTraverse(root):
    '''
    后序遍历
    '''
    if root==None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)

def floor_Traverse(root):
    '''
    层次遍历
    （1）初始化一个队列
    （2）二叉树的根结点放入队列
    （3）重复步骤(4)-(7)直至队列为空
    （4）从队列中取出一个结点x
    （5）访问结点x
    （6）如果x存在左子结点，将左子结点放入队列
    （7）如果x 存在右子结点，将右子结点放入队列
    '''
    if root==None:
        return
    p=[]
    p.append(root)
    while p:
        node=p.pop(0)
        print(node.value)
        if node.left!=None:
            p.append(node.left)
        if node.right!=None:
            p.append(node.right)

if __name__ == "__main__":
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    # root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    print("层次遍历：")
    floor_Traverse(root)
    # print('前序遍历：')
    # preTraverse(root)
    # print('中序遍历：')
    # midTraverse(root)
    # print('后序遍历：')
    # afterTraverse(root)
    