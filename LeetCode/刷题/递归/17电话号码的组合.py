'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #使用递归
        res=[]
        if not digits or set(digits)==0 or set(digits)==1:
            return res
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        n=len(digits)
        def findstr(i,tmp):
            if i==n:
                res.append(tmp)
                return
            for c in dic[digits[i]]:
                findstr(i+1,tmp+c)
        findstr(0,'')
        return res

class Solution(object):
    m = {
        '2':'abc', '3':'def', '4':'ghi',
        '5':'jkl', '6':'mno', '7':'pqrs',
        '8':'tuv', '9':'wxyz'
    }
    def dfs(self, i, digits, ans, tmp):
        if i == len(digits):
            ans.append(''.join(tmp))
            return
        for ch in self.m[digits[i]]:
            tmp.append(ch)
            self.dfs(i+1, digits, ans, tmp)
            tmp.pop()
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        ans = []
        tmp = []
        self.dfs(0, digits, ans, tmp)
        return ans