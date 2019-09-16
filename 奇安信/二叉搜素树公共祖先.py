'''
4
9 6 15 2 -1 12 25 -1 -1 -1 -1 -1 -1 20 37
12 20
'''
class Tree:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def reconbylevel(values,p,q):
    # values=lenstr.split('!')
    def findfa(root,p,q):
        if not root or root==p or root==q:
            return root
        # print(root.val)
        left=findfa(root.left,p,q)
        right=findfa(root.right,p,q)
        if left and right:
            return root
        elif not left:
            return right
        elif not right:
            return left
    index=0
    head=generatenode(values[index])
    index+=1
    queue=[]
    if head:
        queue.append(head)
    node=None
    l=0
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
    print(head.left.val,p.val,q.val)
    tmp=findfa(head,p,q)
    return tmp.val if tmp else -1

def generatenode(val):
    if val==-1:
        return None
    return Tree(val)
def findfa(root,p,q):
    if not root or root==p or root==q:
        return root
    print(root.val)
    left=findfa(root.left,p,q)
    right=findfa(root.right,p,q)
    if left and right:
        return root
    elif not left:
        return right
    elif not right:
        return left

n=int(input())
arr=list(map(int,input().split()))
# print(arr)
a,b=list(map(int,input().split()))
# print(a,b)
a=Tree(a)
b=Tree(b)
# root=reconbylevel(arr)
# p=findfa(root,a,b)
print(reconbylevel(arr,a,b))

