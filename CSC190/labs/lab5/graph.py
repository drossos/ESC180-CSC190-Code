class graph():
    def __init__(self):
        self.adjL = []
    
    def addVertex(self,n):
        for i in range(len(self.adjL),len(self.adjL)+n):
            self.adjL += [[i,[]]]
        return len(self.adjL)
    
    def addEdge(self, from_idx, to_idx, directed,weight):
        if (from_idx < len(self.adjL) and to_idx < len(self.adjL)):
            self.adjL[from_idx][1] += [[to_idx,weight]]
            if (directed == False):
                self.adjL[to_idx][1] += [[from_idx,weight]]
    
    def traverse(self,start,typeBreadth):
        if typeBreadth == True:
            C = queue()
        else: 
            C = stack()
        indLow = start
        if (start == None):
            indLow = 0
        if (start >= len(self.adjL)):
            return []
        output = []
        discovered  = len(self.adjL) * [False]
        processed = len(self.adjL) * [False]
        output = []
        for i in range(indLow,len(self.adjL)):
            temp = []
            if discovered[i] == False:
                C.push(self.adjL[i])
                discovered[i] = True
                curr = []
            while len(C.store) > 0:
                
                curr = C.pop()
                if processed[curr[0]] == False:
                    temp += [curr[0]]
                    processed[curr[0]] = True
                for j in curr[1]:
                    if discovered[j[0]] == False:
                        C.push(self.adjL[j[0]])
                        discovered[j[0]] = True
            if (not temp == []):
                output = output + [temp]
            if (not start == None):
                output = output[0]
                break
        return output
    
    def connectivity(self,vx,vy):
        path0 = self.traverse(vx,True)
        path1 = self.traverse(vy,True)
        retList = [False, False]
        for i in path0:
            if i == vy:
                retList[0] = True
                break
        for i in path1:
            if i == vx:
                retList[1] = True
                break
        return retList

    def path(self,vx,vy):
        path0 = self.traverse(vx,True)
        path1 = self.traverse(vy,True)
        retList0 = []
        retList1 = []
        if vx > vy:
            start = len(path0)-1
            end = 0
            inc = -1
        else:
            start = 0
            end = len(path0)
            inc = 1
        for i in range(start,end,inc):
            retList0 += [path0[i]]
            if i == vy:
                break

        if vy > vx:
            start = len(path1)-1
            end = 0
            inc = -1
        else:
            start = 0
            end = len(path1)
            inc = 1
        for i in range(start,end,inc):
            retList1 += [path1[i]]
            if i == vx:
                break
        if (retList0 == [] or not retList0[len(retList0)-1] == vy):
            retList0 = []
        if (retList1 == [] or not retList1[len(retList1)-1] == vx):
            retList1 = []
        return [retList0, retList1]


class stack():
    def __init__(self):
        self.store = []
    def push(self,val):
        self.store = self.store + [val]
        return True
    def pop(self):

        temp = self.store[len(self.store)-1]
        if (len(self.store) == 1):
            self.store = []
        self.store = self.store[0:len(self.store)-2]
        return temp

class queue():
    def __init__(self):
        self.store = []
    def push(self,val):
        self.store = self.store + [val]
    def pop(self):
        temp = self.store[0]
        if (len(self.store) > 0):
            self.store = self.store[1:len(self.store)]
        else:
            self.store = []
        return temp
        
g = graph()
g.addVertex(5)
g.addEdge(0,2, False, 10)
g.addEdge(2,4, True,3)
temp = g.traverse(0,False)

print(g.traverse(2,True))
print(g.connectivity(2,4))
print(g.connectivity(2,0))
print(g.path(0,4))

