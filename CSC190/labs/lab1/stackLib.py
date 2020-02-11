class Stack:
    def __init__(self):
        self.ls = []
    def push(self, x):
        self.ls = self.ls + [x]
        return 0
    def pop(self):
        if(self.ls != []):
            temp = self.ls[len(self.ls)-1]
            self.ls = self.ls[0:len(self.ls)-1]
            return temp
        else:
            return ""

