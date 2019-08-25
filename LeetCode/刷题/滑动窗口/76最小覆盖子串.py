'''
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

思路：
滑动窗口算法的思路是这样：
1、我们在字符串 S 中使用双指针中的左右指针技巧，初始化 left = right = 0，把索引闭区间 [left, right] 称为一个「窗口」。
2、我们先不断地增加 right 指针扩大窗口 [left, right]，直到窗口中的字符串符合要求（包含了 T 中的所有字符）。
3、此时，我们停止增加 right，转而不断增加 left 指针缩小窗口 [left, right]，直到窗口中的字符串不再符合要求（不包含 T 中的所有字符了）。同时，每次增加 left，我们都要更新一轮结果。
4、重复第 2 和第 3 步，直到 right 到达字符串 S 的尽头。
这个思路其实也不难，第 2 步相当于在寻找一个「可行解」，然后第 3 步在优化这个「可行解」，最终找到最优解。左右指针轮流前进，窗口大小增增减减，窗口不断向右滑动。

链接：https://leetcode-cn.com/problems/two-sum/solution/hua-dong-chuang-kou-suan-fa-tong-yong-si-xiang-by-/

'''
from collections import Counter
def minWindow(s,t):
    #记录最短子串的开始位置和长度
    start=0
    minlen=float('inf')
    left=0
    right=0
    window=Counter(t)
    need=Counter(t)
    for i in t:
        need[i]+=1
    match=0
    while right<len(s):
        c1=s[right]
        if need[c1]:
            window[c1]+=1
            if window[c1]==need[c1]:
                match+=1
        right+=1
        while match==len(need):
            if right-left<minlen:
                #更新最小子串的位置和长度
                start=left
                minlen=right-left
            c2=s[left]
            if need[c2]:
                window[c2]-=1
                if window[c2]<need[c2]:
                    match-=1
            left+=1
    return '' if minlen==float('inf') else s[start:start+minlen]

