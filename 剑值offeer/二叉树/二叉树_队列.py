class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def preTraverse(root):
    '''
    前序遍历
    这里面用到了栈，用栈不断压入根、左孩子，通过pop来回溯父节点，再访问右孩子。
    '''
    if root==None:
        return []
    stack=[]#存储节点的栈
    seq=[]#记录先序访问的序列
    while root or len(stack)!=0:
        if root:
            seq.append(root.value)
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            root=root.right
    
    return seq
    
def midTraverse(root):

    '''
    中序遍历
    '''
    if root==None:
        return []
    stack=[]#存储节点的栈
    seq=[]#记录中序访问的序列
    while root or len(stack)!=0:
        if root:
            # seq.append(root.value)
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            seq.append(root.value)#左孩子先pop出来，再pop根节点
            root=root.right
    
    return seq
def afterTraverse(root):
    '''
    后序遍历
    先序：根左右
    后续：左右根
    即把先序顺序中的 ‘根左右’转换为‘根右左’，然后反过来就变成了‘左右根’。
    '''
    if root==None:
        return []
    stack=[]#存储节点的栈
    seq=[]#记录根右左访问的序列
    output=[]#最终的后续序列
    while root or len(stack)!=0:
        if root:
            seq.append(root.value)
            stack.append(root)
            root=root.right
        else:
            root=stack.pop()
            root=root.left
    while seq:  # 后序遍历 是 将先序遍历的反过来
            output.append(seq.pop())

    return output

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
#层次遍历2
def levelOrder(root):
    # write your code here
    res = []
    # 如果根节点为空，则返回空列表
    if root is None:
        return res
    # 模拟一个队列储存节点
    q = []
    # 首先将根节点入队
    q.append(root)
    # 列表为空时，循环终止
    while len(q) != 0:
        length = len(q)
        for i in range(length):
            # 将同层节点依次出队
            r = q.pop(0)
            if r.left is not None:
                # 非空左孩子入队
                q.append(r.left)
            if r.right is not None:
                # 非空右孩子入队
                q.append(r.right)
            res.append(r.value)
            print(r.value)
    return res

if __name__ == "__main__":
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    # root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    print("层次遍历：")
    floor_Traverse(root)
    print(levelOrder(root))
    print('前序遍历：')
    print(preTraverse(root))
    print('中序遍历：')
    print(midTraverse(root))
    print('后序遍历：')
    print(afterTraverse(root))
    