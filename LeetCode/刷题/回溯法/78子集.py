'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

回溯法：
因为是组合问题，所以我们按顺序读字符，就不需要设置 used 数组；
经过分析，我们知道，在根结点、非叶子结点和叶子结点都需要结算，因此 res.apppend(path[:]) 就要放在“中间”位置。

回溯的过程是执行一次深度优先遍历，一条路走到底，走不通的时候，返回回来，继续执行，一直这样下去，直到回到起点。

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/subsets/solution/hui-su-python-dai-ma-by-liweiwei1419/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []

        res = []
        self.__dfs(nums, 0, [], res)
        return res

    def __dfs(self, nums, start, path, res):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            # 因为 nums 不包含重复元素，并且每一个元素只能使用一次
            # 所以下一次搜索从 i + 1 开始
            self.__dfs(nums, i + 1, path, res)
            path.pop()

'''

'''
class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n=len(nums)
        res=[]
        def helper(idx,tmp):
            res.append(tmp)
            for i in range(idx,n):
                helper(i+1,tmp+[nums[i]])
        helper(0,[])
        return res
    