'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
1
2
3
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

原文：https://blog.csdn.net/qq_41855420/article/details/89357237 
'''
'''
dp[i][j]表示字段s[i,j]是否回文串
状态转移方程：
只有当s[i] == s[j]并且字符段[i + 1, j - 1]是回文串的时候，s[i, j]才能说是回文串
if (s[i] == s[j] && dp[i + 1][j - 1]){
    dp[i][j] = true;
    result += 1;
}
'''
def countSubstrings(s):
    s_le=len(s)
    dp=[[0]*s_le for _ in range(s_le)]
    # //初始化，一个字符是回文串
    for i in range(s_le):
        dp[i][i]=1
    res=s_le#//加上一个字符的回文串
    for i in range(s_le-2,-1,-1):
        if s[i]==s[i+1]:
            # //处理"aa"这种连续的两个字符回文串
            dp[i][i+1]=1
            print(s[i:i+2])
            res+=1
        # //处理[i, j]长度超过2的区间段
        for j in range(i+2,s_le,1):
            # //只有当s[i] == s[j]并且字符段[i + 1, j - 1]是回文串的时候，s[i, j]才能说是回文串
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j]=1
                print(s[i:j+1])
                res+=1
    print(dp)
    return res

def countSubstrings2(s):
        if not s or len(s)==0:
            return 0
        count=0
        s1=manale(s)
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
        return count
def manale(s):
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

a='aaa'
print(countSubstrings2(a))

#中心拓展法
def countSubstrings1(s):
    res=1
    n=len(s)
    if n==0:
        return 0
    for i in range(1,n,1):
        left=i
        right=i
        #以i为中心进行拓展
        while left>=0 and right<n and s[left]==s[right]:
            res+=1
            left-=1
            right+=1
        left=i-1
        right=i
        #以i-1进行拓展
        while left>=0 and right<n and s[left]==s[right]:
            res+=1
            left-=1
            right+=1
    return res