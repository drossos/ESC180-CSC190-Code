from random import *
class conway:
    def __init__(self,num1,num2,opt):
        if opt == 'zeros':
            self.randopt = 0
        elif opt == "ones":
            self.randopt = 1
        else:
            self.randopt = 2
        self.store = []
        for i in range(0,num1,1,):
            temp = []
            for k in range(0,num2,1):
                val = self.randopt
                if self.randopt ==2:
                    val = randint(0,1)
                temp += [val]
            self.store += [temp]
   
    def evolve(self,rule):
        nextState = [[0]*len(self.store[0])]* len(self.store)
        blah = list(self.store)
        for i in range(0,len(self.store),1):
            for j in range(0,len(self.store[0]),1):
                nextState[i][j] = rule(self.store[i][j],self.getNeighbours(i,j))
            blah[i] = list(nextState[i])
        self.store = blah
         
        return True
 
    def getDisp(self):
        tempStr = ""
        for i in self.store:
            for j in i:
                if j == 0:
                    tempStr += " "
                elif j == 1:
                    tempStr += "*"
            tempStr += "\n"
        return tempStr

    def printDisp(self):
        print(self.getDisp())
        return True
    
    def setPos(self,row,col,val):
        if val == 1 or val == 0 and row < len(self.store) and col < len(self.store[0]):
            self.store[row][col] = val
            return True
        else:
            return False

    def getNeighbours(self,row,col):
        nbs = []
        if row == len(self.store) - 1:
            rowUpper = 0
            rowLower = row-1
        elif row == 0:
            rowLower = len(self.store)-1
            rowUpper = row +1
        else:
            rowLower = row-1
            rowUpper = row+1

        if col == len(self.store[0]) - 1:
            colUpper = 0
            colLower = col -1
        elif col == 0:
            colLower = len(self.store[0])-1
            colUpper = col +1
        else:
            colLower = col-1
            colUpper = col+1

        for i in range(0,len(self.store),1):
            for j in range(0,len(self.store[0]),1):
                if (i == rowUpper or i == rowLower or i == row) and (j == colLower or j == colUpper or j == col):
                    if not (i == row and j == col):
                        nbs += [self.store[i][j]]

        return nbs               
