'''
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。
示例 1 :
输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
示例 2 :
输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 :
输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。

思路：
单调栈的另一个应用，思想为删除靠前的较大的数能够使得最后的数值最小。 构建递增栈，
若当前数字小于栈顶元素，则在满足待删减字符数不为0的情况下，栈顶元素出栈，当前数字入栈。
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num or k<=0:
            return num
        stack=[]
        count=0
        for value in num:
            if not stack or value>=stack[-1] or count>=k:
                stack.append(value)
            else:
                while stack and value<stack[-1] and count<k:
                    stack.pop()
                    count+=1
                stack.append(value)
        while count<k:
            stack.pop()
            count+=1
        if not stack:
            return '0'
        return '%d'%int(''.join(stack))
'''
贪心算法
将原整数的所有数字从左到右进行比较，如果发现某位一个位数大于它后面的数字那么删除该数字后，比赛使该数字的值下降
时间和空间复杂度都是o(n)
'''
def removeKdigits(num,k):
    res=''
    for i in num:
        while len(num) and k and res[-1]>i:
            res=res[:-1]
            k-=1
        if len(ans) or i!='0':
            res=res+i
    while len(res) and k:
        res=res[:-1]
        k-=1
    return res if len(res) else '0'