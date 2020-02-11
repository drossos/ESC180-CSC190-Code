class Queue:
    def __init__(self):
        self.store = []
    def dequeue(self):
        temp = self.store[0]
        self.store = self.store[1:]
        return temp
    def enqueue(self,val):
        self.store = self.store + [val]
        return 0;
    def isEmpty(self):
        if len(self.store) == 0:
            return True
        else:
            return False
