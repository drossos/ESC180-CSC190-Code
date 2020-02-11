
class Stack:
    def __init__(self):
        self.store = []
    def pop(self):
        temp = self.store[0]
        self.store = self.store[1:]
        return temp
    def push(self,val):
        self.store = [None] + self.store
        self.store[0] = val
        return 0;
    def isEmpty(self):
        if len(self.store) == 0:
            return True
        else:
            return False
