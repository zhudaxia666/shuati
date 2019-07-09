'''
利用两个堆栈，一个叫输入栈，一个叫输出栈。用于实现进入队列Push(x)，出队列pop()，查看最后一个元素peek()，及判断是否为空empty()函数。每次从输入栈进，输出栈出。
push操作：将加入的元素添加到输入栈；
pop操作：从输出栈取走元素，输出栈没有元素时，将输入栈元素依次出栈压入输出栈，再从输出栈取出；
peek操作：同pop操作原理一样；
empty为真的条件是两个栈都为空。

'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackin = []
        self.stackout = []
        
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stackin.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stackin and not self.stackout:
            return True
        else:
            return False

#使用一个列表
class MyQueue1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        #print(f"stack:{self.stack}")
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop(0)
        
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack)==0