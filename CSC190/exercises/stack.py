class stack:
    def __init__(self):
        self.stck = []

    def put(self,val):
        self.stck = [val] + self.stck
    
    def pop(self):
        temp = self.stck[0]
        self.stck = self.stck[1:]
        return temp



temp = stack()
temp.put(50)
temp.put(30)

print(str(temp.pop()) + " ")
print(temp.pop())
