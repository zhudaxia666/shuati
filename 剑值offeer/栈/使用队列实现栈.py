'''
这里我们使用两个队列来实现栈。我们首先定义了一个队列类（Queue），具有入队（push）和出队（pop）两个方法，以及队列长度（length）和队列是否为空（is_empty）两个属性：
push()：元素入队成为队尾，没有返回值；
pop()：队头元素出队，返回值为出队元素；
length：获得当前队列长度；
is_empty：获得当前队列是否为空，如果为空返回True。

首先，我们实例化一个基本队列queue1和一个辅助队列queue2，每次操作后，基本队列中的元素就是栈中的元素，辅助队列用于每一步操作中帮助实现元素暂存的功能。栈的每一个方法这样实现：
push()：元素入栈，直接在基本队列queue1中加入元素即可；
pop()：弹出栈顶元素，将基本队列queue1中的每次元素出队并依次加入辅助队列queue2中，当只剩下一个元素res时，把这个元素拿出来，不加入queue2，然后把辅助队列queue2中的所有元素依次返还基本队列queue1，并返回之前被拿出来的元素res即可。
top()：获取栈顶元素，实现方法与pop十分相似，唯一只是res会被再加入到queue2中；
empty()：判断栈是否为空，栈为空与基本队列queue1为空的判断结果完全一致，因此直接返回queue1的is_empty方法即可。

'''
class Mystack(object):
    def __init__(self):
        self.queue1=[]
        self.queue2=[]
    def push(self,x):
        self.queue1.append(x)
    def pop(self):
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.pop(0))
        res=self.queue1.pop()
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return res
    def top(self):
        while len(self.queue1)>1:
            self.queue2.append(self.queue2.pop(0))
        res=self.queue1.pop()
        self.queue2.append(res)
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return res
    def empty(self):
        return len(self.queue1)==0
