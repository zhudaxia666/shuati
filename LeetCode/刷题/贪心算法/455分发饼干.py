'''
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，
都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
注意：
你可以假设胃口值为正。
一个小朋友最多只能拥有一块饼干。
输入: [1,2,3], [1,1]

输出: 1

解释: 
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。

贪心算法
Step1 给孩子和饼干都排序
Step2 分别维护一个index
Step3 策略：如果当前饼干可以满足胃口，则count 和 两个index加一，否则饼干的index加一(更大的饼干)
'''
#如果小的饼干满足不了贪心指数小的小朋友，就放弃这个小的饼干。例如：g=[2, 3], s=[1, 2, 3]。
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gi = 0
        si = 0
        res = 0

        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                si += 1
                gi += 1
                res += 1
            else:
                si += 1
        return res

#如果最大的饼干都满足不了这个最贪心的小朋友，就放弃这个小朋友。例如：g=[4, 1], s=[3, 2, 1]。
class Solution2:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        gi = 0
        si = 0
        res = 0

        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                si += 1
                gi += 1
                res += 1
            else:
                gi += 1
        return res