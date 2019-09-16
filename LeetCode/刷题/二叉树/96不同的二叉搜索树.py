'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode/
标签：动态规划
假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)

当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，则
f(i) = G(i-1)*G(n-i)f(i)=G(i−1)∗G(n−i)

综合两个公式可以得到 卡特兰数 公式

G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
'''
def numtree(n):
    G=[0]*(n+1)
    G[0]=1
    G[1]=1
    for i in range(2,n+1):
        for j in range(1,i+1):
            G[i]+=G[i-1]*G[i-j]
    return G[n]