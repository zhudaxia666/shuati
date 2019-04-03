'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
思路
使用两个stack，一个为数据栈，另一个为辅助栈。数据栈用于存储所有数据，辅助栈用于存储最小值。
举个例子：
入栈的时候：首先往空的数据栈里压入数字3，显然现在3是最小值，我们也把最小值压入辅助栈。接下来往数据栈里压入数字4。
由于4大于之前的最小值，因此我们只要入数据栈，不压入辅助栈。
出栈的时候：当数据栈和辅助栈的栈顶元素相同的时候，辅助栈的栈顶元素出栈。否则，数据栈的栈顶元素出栈。
获得栈顶元素的时候：直接返回数据栈的栈顶元素。
栈最小元素：直接返回辅助栈的栈顶元素。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        self.stack1.append(node)
        if self.stack2==[] or self.stack2[-1]>node:
            self.stack2.append(node)
        # write code here
    def pop(self):
        # write code here
        if self.stack1==[]:
            return None
        else:
            if self.stack1[-1]==self.stack2[-1]:
                self.stack2.pop()
            return self.stack1.pop()
    def top(self):
        return self.stack1[-1]
    def min(self):
        return self.stack2[-1]


"""
下面是别人的：
"""
# -*- coding:utf-8 -*-
class Solution1:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)
    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_stack[-1]


