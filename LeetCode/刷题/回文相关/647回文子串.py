'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
示例 1:
输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:
输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
'''
'''
马拉车算法
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s or len(s)==0:
            return 0
        count=0
        s1=self.manale(s)
        print(s1)
        p=[0]*len(s1)
        c=-1
        r=-1
        for i in range(len(s1)):
            p[i]=min(p[2*c-i],r-i) if r>i else 1
            while i+p[i]<len(s1) and i-p[i]>=0:
                if s1[i+p[i]]==s1[i-p[i]]:
                    p[i]+=1
                else:
                    break
            if i+p[i]>r:
                r=i+p[i]
                c=i
            count+=p[i]//2
        print(p)
        return count
    def manale(self,s):
        n=len(s)
        res=[0]*(2*n+1)
        index=0
        for i in range(len(res)):
            if i%2==0:
                res[i]="#"
            else:
                res[i]=s[index]
                index+=1
        return res
a=Solution()
a.countSubstrings('aaa')