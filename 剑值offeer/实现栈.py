class stack():
    def __init__(self):
        self.stack=[]
    def empty(self):
        return self.stack==[]

    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.empty():
            return None
        else:
            return self.stack.pop(-1)
    def top(self):
        if self.empty():
            return None
        else:
            return self.stack[-1]
    def length(self):
        return len(self.stack)

'''
一个列表实现两个栈
'''
class Twostacks(object):
    def __init__(self):
        self.stack=[]
        self.a_size=0
        self.b_size=0
        self.top=0
    def a_isEmpty(self):
        return self.a_size==0
    def a_push(self,item):
        self.stack.insert(self.a_size,item)
        self.a_size+=1       
    def a_pop(self):
        if self.a_size>=1:
            item=self.stack[self.a_size-1]
            self.stack.remove(item)
            self.a_size-=1
            return item
    def b_isEmpty(self):
        return self.b_size==0
    def b_push(self,item):
        self.stack.insert(self.a_size,item)
        self.b_size+=1
    def b_pop(self):
        if self.b_size>=1:
            item=self.stack[self.a_size]
            self.stack.remove(item)
            self.b_size-=1
            return item