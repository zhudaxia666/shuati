class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
 
def _find_parent(nodes, i):
    i_parent = -1
    max_min_val = -float('inf')
    for j in range(i):
        if max_min_val < nodes[j].val < nodes[i].val:
            max_min_val = nodes[j].val
            i_parent = j
    return i_parent
 
 #先构建树
def gen_bst(arr, n):
    if not arr:
        return
    nodes = []
    for num in arr:
        nodes.append(BinaryTreeNode(num))
    for i in range(1, n):
        if nodes[i].val < nodes[i - 1].val:
            nodes[i - 1].left = nodes[i]
        else:
            i_parent = _find_parent(nodes, i)
            nodes[i_parent].right = nodes[i]
    return nodes[0]
 
 
def level_order(root):
    ret = []
    if not root:
        return ret
    queue = [root]
    while queue:
        cur = queue.pop(0)
        ret.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return ret
 
 
if __name__ == '__main__':
    arr = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    n = 9
    root = gen_bst(arr, n)
    ret = level_order(root)
    print(' '.join([str(num) for num in ret]))