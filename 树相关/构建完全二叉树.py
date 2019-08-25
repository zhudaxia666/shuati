'''
 输入一个数字n，构建一个完全二叉树并输出。例如输入n=5，二叉树的结构为：
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def creatTree(n):
    if n<1:
        return None
    num=list(range(1,n+1))
    root=Node(num[0])
    index=1
    stack=[root]
    while stack:
        root=stack.pop(0)
        if index<n+1:
            root.left=Node(num[index])
            stack.append(Node(num[index]))
            index+=1
        else:
            break
        if index<n+1:
            root.left=Node(num[index])
            stack.append(Node(num[index]))
            index+=1
        else:
            break
    
