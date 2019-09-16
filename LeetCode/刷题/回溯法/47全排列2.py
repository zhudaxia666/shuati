'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

当数组中有重复元素的时候，可以先将数组排序，排序以后在递归的过程中可以很容易发现重复的元素。当发现重复元素的时候，让这一个分支跳过，以达到“剪枝”的效果，重复的排列就不会出现在结果集中。

下面这个代码片段：

if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
    continue;
}
中的 used[i - 1] 加或者不加 ! ，提交到力扣的代码测评系统中都是可以通过的，下面我解释一下原因。

以 [2, 3, 3, 3] 中的 3 个 3 为例，相同的 3 个 3 有 6 个排列。我们只要保留 1 个就好了。

它们的索引分列是：

[1, 2, 3] （数组中的数组表示 3 这个元素在 [2, 3, 3, 3] 这个数组中的索引，在全排列中可能的“排列”，下同）
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
发现其实又是一个全排列问题。首先联系数组 used[i - 1] 的语义：used[i - 1] == true 表示索引 i 位置的前一个位置元素已经使用过。在 used[i - 1] == true 的时候全部 continue 掉，则只剩下了 used[i - 1] == false 的情况，即当前遍历的元素的之前的元素均未使用过，因此保留了 [3, 2, 1] 这种排列。

反之理解另一种情况。

因此，used[i - 1] 前面加不加感叹号的区别仅在于保留的是相同元素的顺序索引，还是倒序索引；应用于本题，则是相同分支保留的是第 1 个分支还是最后一个分支，它们在结果集中是“等价的”，具体加感叹号对应哪种情况，不加感叹号，对应哪种情况，我个人觉得并不太重要。

以下代码根据我在「力扣」第 46 题：全排列 II 中的题解（上文有给出链接）中的示例代码修改而来，具体修改的地方，在下面代码的注释中有说明。

基于第 46 题，做 2 处修改即可：

1、在开始回溯算法之前，对数组进行一次排序操作，这是上面多次提到的；

2、在进入一个新的分支之前，看一看这个数是不是和之前的数一样，如果这个数和之前的数一样，并且之前的数还未使用过，那接下来如果走这个分支，就会使用到之前那个和当前一样的数，就会发生重复，此时分支和之前的分支一模一样。（这句话特别关键，可以停下来多看两遍，再看一看上面画的那张图）。

链接：https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
'''
class Solution:
    def permuteUnique(self,nums):
        if len(nums)==0:
            return []
        #修改 1：首先排序，之后才有可能发现重复分支，升序、倒序均可
        nums.sort()
        used=[False]*len(nums)
        res=[]
        self.dfs(nums,[],used,res)
        return res
    def dfs(self,nums,tmp,used,res):
        if len(tmp)==len(nums):
            res.append(tmp.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                #因为排序以后重复的数一定不会出现在开始，故 i > 0
                # 和之前的数相等，并且之前的数还未使用过，只有出现这种情况，才会出现相同分支
                # 这种情况跳过即可
                if i>0 and nums[i]==nums[i-1]:
                    continue
                used[i]=True
                tmp.append(nums[i])
                self.dfs(nums,tmp,used,res)
                used[i]=False
                tmp.pop()

class Solution1:
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return []

        # 修改 1：首先排序，之后才有可能发现重复分支，升序、倒序均可
        nums.sort()
        # nums.sort(reverse=True)

        used = [False] * len(nums)
        res = []
        self.__dfs(nums, 0, [], used, res)
        return res

    def __dfs(self, nums, index, pre, used, res):
        if index == len(nums):
            res.append(pre.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                # 修改 2：因为排序以后重复的数一定不会出现在开始，故 i > 0
                # 和之前的数相等，并且之前的数还未使用过，只有出现这种情况，才会出现相同分支
                # 这种情况跳过即可
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                pre.append(nums[i])
                self.__dfs(nums, index + 1, pre, used, res)
                used[i] = False
                pre.pop()
#对比46题，只需添加判断前后是否相等，若nums[i] == nums[i - 1],则此情况前面已经讨论过，因此continue就好；需要事先对nums进行排序！
class Solution3:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        res = []
        
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
        backtrack(nums, [])  
        return res