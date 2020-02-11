class Queue:
    def __init__(self):
        self.ls = []
    def enqueue(self,ele):
        self.ls = self.ls + [ele]
    def dequeue(self):
        temp = self.ls[0]
        self.ls = self.ls[1]
        return temp
    def empty(self):
        if (len(self.ls) == 0):
            return True
        else:
            return False


def traverse_breadth(T):

     x=Queue()
     x.enqueue(T)
     while x.empty() == False:

          r=x.dequeue()

          print(r[0])

          for i in r[1:len(r)]:

               x.enqueue(i)
