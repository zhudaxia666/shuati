 '''
 使用数组表示大小固定的队列和栈
 思路：
 表示队列时，
 设置三个指针start，end,size分别表示队头，队尾和队列元素个数
 进队操作，如果size等于数组长度，报错，否则size++,如果队尾end==len(nums)-1,则last=0,否则last+1
 出队操作，如果size为0，报错，否则，size--，如果队头first==len(nums)-1,first=0,否则fist+1

 表示栈时，类似
 '''
 class Queue(object):
     def __init__(self):
         self.queue=[]
         self.size=0
         self.start=0
         self.end=0
    def push(self,val):
        if self.size==len(self.queue):
            return
        self.size+=1
        self.queue[self.end]=val
        if self.end==len(self.queue)-1:
            self.end=0
        else:
            self.end+=1
    def poll(self):
        if self.size==0:
            return
        self.size-=1
        tmp=self.start
        if self.start==len(self.queue)-1:
            self.start=0
        else:
            self.first+=1
        return self.queue[tmp]
    def peek(self):
        if self.size==0:return None
        return self.queue[first]

