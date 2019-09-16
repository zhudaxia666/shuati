'''
1，实现二叉树的先中后遍历，包括递归和非递归
2.直观打印一棵树
3，求中序遍历后继节点（有右子树后继一定是右子树最左边的节点，无右子树向找，找到当前节点是父节点的左子树，则父节点就是原始节点的后继）
4.二叉树序列化和反序列化
5.判断一个数是否是平衡二叉树，搜索二叉树，完全二叉树（树形DP，avl数，红黑树不用事现）
6，已知一个完全二叉树，求其节点的个数，时间复杂度低于O（n）
'''
'''
1.先中后遍历非递归版，
先序遍历：首先建立一个栈，根节点先进栈，然后弹出栈，如果其右子树存在，进栈，左子树存在进栈，然后重复这个过程循环出进栈。核心：进栈顺序 根右左
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
#先序
def preorder(root):
    res=[]
    if not root:
        return None
    else:
        stack=[]
        stack.append(root)
        while len(stack)>0:
            root=stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
    return res
#中序,首先判断栈是否为空或头结点是否为空，若头结点不为空，就遍历左子树，如果左子树不为空，进栈，直到左子树为空。此时弹出栈顶，遍历栈顶节点的右子树。重复上面的过程
def inorder(root):
    res=[]
    if root:
        stack=[]
        while len(stack)>0 or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                res.append(root.val)
                root=root.right

#后序遍历，和前序遍历相似，后序遍历是左右根，如果前序是根左右，如果把遍历顺序变成根右左，最后再翻转过来
def afterorder(root):
    res=[]
    if root:
        stack=[]
        stack.append(root)
        while len(stack)>0:
            root=stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]
'''
3.后继结点
'''
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.parent=None

def getsuccessndoe(root):
    if not root:
        return root
    if root.right:
        root=root.right
        while root.left:
            root=root.left
        return root
    else:
        parent=root.parent
        while parent and parent.left!=root:
            root=root.parent
            parent=root.parent
        return parent
'''
4.序列化和反序列化。序列化就是讲二叉树以某种形式存储，例如字符串。反序列化是二叉树就序列化形式的字符串，转换成二叉树的形式
'''
#前序遍历版。空结点用#表示，每个节点以！结尾
#递归版前序序列化
def preserial(root):
    if not root:
        return "#!"
    res=str(root.val)+'!'
    res+=preserial(root.left)
    res+=preserial(root.right)
    return res
#反序列化
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def reconpreserial(prestr):
    values=prestr.split('!')
    queue=[]
    for i in range(len(values)):
        queue.append(values[i])
    return reconpreorder(queue)
def reconpreorder(queue):
    value=queue.pop(0)
    if value=='#':
        return Node
    head=Node((int(value))
    head.left=reconpreorder(queue)
    head.right=reconpreorder(queue)
    return head

'''
序列化 层次遍历
'''
def serialbylevel(root):
    if not root:
        return '#!'
    res=root.val+'!'
    queue=[]
    queue.append(root)
    while len(queue)!=0:
        root=queue.pop(0)
        if root.left:
            res+=root.left.val+'!'
            queue.append(root.left)
        else:
            res+='#!'
        if root.right:
            res+=root.right.val+'!'
            queue.append(root.right)
        else:
            res+='#!'
    return res
#反序列化
def reconbylevel(lenstr):
    values=lenstr.split('!')
    index=0
    head=generatenode(values[index])
    index+=1
    queue=[]
    if head:
        queue.append(head)
    node=None
    while len(queue)>0:
        node=queue.pop(0)
        node.left=generatenode(values[index])
        index+=1
        node.right=generatenode(values[index])
        index+=1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return head

def generatenode(val):
    if val=='#':
        return None
    return Node(val)

'''
5，判断一棵树是否是平衡二叉树
'''
def isbanlanced(root):
    if not root:
        return True
    if abs(treedepth(root.left)-treedepth(root.right))>1:
        return False
    return isbanlanced(root.left) and isbanlanced(root.right)
def treedepth(root):
    if not root:
        return 0
    left=treedepth(root.left)
    right=treedepth(root.right)
    return max(left,right)+1
'''
左神版
'''
class returndata:
    def __init__(self,isb,h):#两个值分别表示是否是平衡树，和高度
        self.isb=isb
        self.h=h
def idB(root):
    return process(root).isb
def process(root):
    if not root:
        return returndata(True,0)
    leftdata=process(root.left)
    if leftdata.isb==0:
        return returndata(False,0)
    rightdata=process(root.right)
    if rightdata.isb==0:
        return returndata(False,0)
    if abs(leftdata.h-rightdata.h)>1:
        return returndata(False,0)
    return returndata(True,max(leftdata.h,rightdata.h)+1)



'''
判断一棵树是否是二叉搜索树BST
将中序打印换成比较
'''
def isBST(head):
    if not head:
        return True
    stack=[]
    pre=-float('inf')
    while stack or head!=None:
        if head:
            stack.append(head)
            head=head.left
        else:
            head=stack.pop()
            if head.val>pre:
                pre=head.val
                head=head.right
            else:
                return False
    return True
'''
判断是否是完全二叉树
'''
def isCBT(head):
    if not head:
        return True
    queue=[]
    leaf=False
    l=None
    r=None
    queue.append(head)
    while queue:
        head=queue.pop(0)
        l=head.left
        r=head.right
        if (leaf and (l!=None or r!=None)) or (l==None and r!=None):#如果是叶子节点但左右有不为空的，或左子树为空但右子树不为空
            return False
        if l:
            queue.append(l)
        if r:
            queue.append(r)
        else:
            leaf=True
    return True
'''
6.已知一个完全二叉树，求其节点的个数，时间复杂度低于O（n）
思路：首先统计二叉树的高度，然后判断右子树的左边界是否到达最后一层，如果到达最后一层，那左子树一定是满的，此时左子树节点个数为2^(h-l)-1+1,+1是加上根节点，然后递归遍历右子树
如果右子树的左边界不在最后一层，则右子树一定是满的，此时右子树节点个数是2^(h-l-1)-1+1
时间复杂度O(logn)^2
'''
def nodeNum(head):
    if not head:
        return 0
    return bs(head,1,mostLeftlevel(head,1))
def bs(node,l,h):#l表示node在第几层
    if l==h:
        return 1
    if mostLeftlevel(node.right,l+1)==h:
        return (1 << (h-l)) + bs(node.right,l+1,h)
    else:
        return (1 << (h-l-1)) + bs(node.left,l+1,h)

def mostLeftlevel(node,level):
    while node:
        level+=1
        node=node.left
    return level-1

