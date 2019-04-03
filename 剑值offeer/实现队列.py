class queue():
    def __init__(self):
        self.queue=[]
    def empty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.append(data)
    def delqueue(self):
        if self.empty():
            return None
        else:
            return self.queue.pop(0)
    def head(self):
        if self.empty():
            return None
        else:
            return self.queue[0]
    def length(self):
        return len(self.queue)