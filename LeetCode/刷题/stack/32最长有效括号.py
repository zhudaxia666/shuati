'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''
'''
栈：
与找到每个可能的子字符串后再判断它的有效性不同，我们可以用栈在遍历给定字符串的过程中去判断到目前为止扫描的子字符串的有效性
同时能的都最长有效字符串的长度。我们首先将 -1 放入栈顶。
对于遇到的每个‘(’ ，我们将它的下标放入栈中。
对于遇到的每个‘)’ ，我们弹出栈顶的元素并将当前元素的下标与弹出元素下标作差，得出当前有效括号字符串的长度
通过这种方法，我们继续计算有效子字符串的长度，并最终返回最长有效子字符串的长度。
时间复杂度：O(n)
空间复杂度：O(n)
'''
def longest(s):
    maxlen=0
    stack=[]
    stack.append(-1)
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                maxlen=max(maxlen,i-stack[-1])
    return maxlen
'''
不需要额外的空间

在这种方法中，我们利用两个计数器 left 和 right 。首先，我们从左到右遍历字符串，对于遇到的每个‘(’，
我们增加 left 计算器，对于遇到的每个‘)’ ，我们增加 right 计数器。每当 left 计数器与 right 计数器相等时，
我们计算当前有效字符串的长度，并且记录目前为止找到的最长子字符串。如果 right 计数器比 left计数器大时，
我们将 left 和 right 计数器同时变回 0 。
'''
def longestval(s):
    left=0
    right=0
    maxlen=0
    for i in range(len(s)):
        if s[i]=='(':
            left+=1
        else:
            right+=1
        if left==right:
            maxlen=max(maxlen,2*right)
        elif right>left:
            left=right=0
    left=right=0
    for i in range(len(s),-1,-1):
        if s[i]=='(':
            left+=1
        else:
            right+=1
        if left==right:
            maxlen=max(maxlen,2*left)
        elif left>right:
            left=right=0
    return maxlen