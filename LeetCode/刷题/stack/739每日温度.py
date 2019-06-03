'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高的天数。如果之后都不会升高，请输入 0 来代替。
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的都是 [30, 100] 范围内的整数。
'''
'''
思路：
维护递减栈，后入栈的元素总比栈顶元素小。
比对当前元素与栈顶元素的大小
若当前元素 < 栈顶元素：入栈
若当前元素 > 栈顶元素：弹出栈顶元素，记录两者下标差值即为所求天数
这里用栈记录的是 T 的下标。
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        results=[0]*len(T)
        stack=[]
        for k,value in enumerate(T):
            if stack:
                while stack and T[stack[-1]]<value:
                    results[stack[-1]]=k-stack[-1]
                    stack.pop()
            stack.append(k)
        return results

# #方法2
# class Solution1(object):
#     def dailyTemperatures(self, T):
#         stack, r = [], [0] * len(T)
#         for i, t in enumerate(T):
#             while stack and T[stack[-1]] < t: 
#                 r[stack.pop()] = i - stack[-1]
#             stack.append(i)
#         return r