


class Queue:
    def __init__(self):
        ls = []
    def dequeue(self):
        temp = self.ls[len(self.ls)-1]
        self.ls = self.ls[0:len(self.ls)-1]
        return temp
    def enqueue(self,element):
        self.ls = self.ls + [element]
        return 0
    def empty(self):
        if (len(self.ls) == 0):
            return True
        return False

def traverse_breadth(T):
    x = Queue()
    x.enqueue(T)
    while (x.empty() == False):
        r = x.dequeue()
        print(r[0])
        for i in r[1:len(r)]:
            x.enqueue(i)


