'''
思路：
由于每个节点只有唯一一个父节点，我们可以使用字典的v-k的形式
字典中初始根节点的父节点为none
字典建立完成后，二叉树就可以看成一个所有节点都将最终指向根节点的链表

于是二叉树中寻找两个节点的最小公共节点就相当于在一个链表中寻找他们相遇的节点

'''
def lowestCommon(root,p,q):
    dic={root:None}
    def dfs(node):
        if node:
            if node.left:
                dic[node.left]=node
            if node.right:
                dic[node.right]=node
            bfs(node.left)
            bfs(node.right)
    dfs(root)
    l1,l2=p,q
    while l1!=l2:
        l1=dic.get(l1) if l1 else p
        l2=dic.get(l2) if l2 else q
    return l1