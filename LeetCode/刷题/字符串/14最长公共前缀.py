'''
先统计strs中最短字符串长度min，之后用min做判断边界；
判断[0,min]范围内，所有字符串的公共头部，若发现不同则直接返回；
若[0,min]范围内所有字符串相同则直接返回。min == 0需要做特殊处理。
'''
def longestCommonPrefix1(s):
    if not s:return ''
    mi=len(s[0])
    for i in s[1:]:
        mi=min(mi,len(i))
    for i in range(mi):
        for j in range(len(s)-1):
            if s[j][i]!=s[j+1][i]:
                return s[j][:i]
    return s[0][:i+1] if mi else ""


s=["flower","faowe","floght"]
print(longestCommonPrefix1(s))

