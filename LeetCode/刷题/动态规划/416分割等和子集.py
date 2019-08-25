'''
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
 
示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
'''
'''
思路：
这是一道以 0-1 背包问题为背景的算法练习题，我们把这个题目翻译一下：
给定一个只包含正整数的非空数组。是否可以从这个数组中挑选出一些正整数，每个数只能用一次，使得这些数的和等于整个数组元素的和的一半。
0-1 背包问题也是最基础的背包问题，它的特点是：待挑选的物品有且仅有一个，可以选择也可以不选择。下面我们定义状态，不妨就用问题的问法定义状态试试看。
dp[i][j]：表示从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和等于 j。
根据我们学习的 0-1 背包问题的状态转移推导过程，新来一个数，例如是 nums[i]，根据这个数可能选择也可能不被选择：
如果不选择 nums[i]，在 [0, i - 1] 这个子区间内已经有一部分元素，使得它们的和为 j ，那么 dp[i][j] = true；
如果选择 nums[i]，在 [0, i - 1] 这个子区间内就得找到一部分元素，使得它们的和为 j - nums[i] ，我既然这样写出来了，
你就应该知道，这里讨论的前提条件是 nums[i] <= j。
以上二者成立一条都行。于是得到状态转移方程是：
dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]], (nums[i] <= j)
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/
'''
def canPartition(nums):
    size=len(nums)
    #如果整个数组和不是偶数，就无法平分
    s=sum(nums)
    if s%2==1:
        return False
    #二维dp问题：背包的容量
    target=s//2
    dp=[[False for _ in range(target+1)] for _ in range(size)]
    #先写第1行看看第一行数是不是能够刚好填满容量为target
    for i in range(target+1):
        dp[0][i]=False if nums[0]!=i else True
    #i表示物品索引
    for i in range(1,size):
        #j表示容量
        for j in range(target+1):
            if j>=nums[i]:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i]]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
'''
复杂度分析：
时间复杂度：O(NC)O(NC)：这里 NN 是数组元素的个数，CC 是数组元素的和的一半。
空间复杂度：O(NC)O(NC)。
'''
#使用回溯法
def canPartition(self, nums) -> bool:
        #回溯思想: 先排序数组来减少回溯的节点, 然后通过递归, 遍历所有的可能
        s=sum(nums)
        # 假设可以拆分为两个和相等的子集, 数组的和是子集和的两倍, 一定是偶数
        if s%2==1:
            return False
        n=len(nums)
        nums_sorted=sorted(nums,reverse=True)
        #假设可以找到和为整个数组和一半的子集, 那么剩下的就是另一个子集
        def findPart(remain,index):
            if remain==0:
                return True
            if index<n and remain<nums_sorted[index]:
                return False
            for i in range(index,n):
                 # !!! 回溯的节点, 不停的枚举试错, 一旦成功返回true
                if findPart(remain-nums_sorted[i],i+1):
                    return True
            return False
        return findPart(s//2,0)
