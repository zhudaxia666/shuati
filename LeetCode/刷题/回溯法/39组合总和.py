'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''
'''
思路：回溯法
很标准的模板
'''
def combina(candidates,target):
    candidates.sort()
    n=len(candidates)
    res=[]
    def helper(i,tem_sum,tmp):
        if tem_sum>target or i==n:
            return
        if tem_sum==target:
            res.append(tmp)
            return
        helper(i,tem_sum+candidates[i],tmp+[candidates[i]])
        helper(i+1,tem_sum,tmp)
    helper(0,0,[])
    return res

def combina1(candidates,target):
    candidates.sort()
    n=len(candidates)
    res=[]
    def helper(i,tem_sum,tmp):
        if tem_sum>target or i==n:
            return
        if tem_sum==target:
            tmp.append(tmp)
            return
        for j in range(i,n):
            if tem_sum+candidates[j]>target:
                break
            helper(j,tem_sum+candidates[j],tmp+[candidates[j]])
    helper(0,0,[])
    return res