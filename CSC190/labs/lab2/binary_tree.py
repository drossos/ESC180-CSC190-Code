from queue import *
import tree
from stack import *
class binary_tree:
    def __init__(self,x):
        self.store = [x]

    def AddLeft(self,x):
        if len(self.store) == 1:
            self.store = self.store + [x] + [None]
        elif len(self.store) > 0:
            self.store[1] = x                                                                                                                                                           
        return True
    
    def AddRight(self,x):
        if len(self.store) == 1:
            self.store = self.store + [None] + [x]
        elif len(self.store) > 0:
            self.store[2] = x                                                                                                                                                           
        return True

    def Get_LevelOrder(self):
        que = Queue()
        tStr = []
        que.enqueue(self.store)
        
        while (not(que.isEmpty())):
        
            temp = que.dequeue()
            if(True):
                name = temp[0]
                #print(temp)
                tStr = tStr + [name]
            for i in range(1,len(temp)):
                if(not temp[i] == None):
                    que.enqueue(temp[i].store)
        return tStr

    def ConvertToTree(self):
        if (len(self.store) > 1 and not(self.store[2] == None)):
            return [False, None]
        stk = Stack()
        newTree = tree.tree(self.store[0])
        currTree = newTree
        trStk = Stack()
        trStk.push(currTree)
        currBT = self
        stk.push(currBT)

        while(True):
            if(stk.isEmpty()):
                return [True,newTree]
            currBT = stk.pop()
            currTree = trStk.pop()
            #print(currBT.store)
            if (len(currBT.store)>1 and not currBT.store[1] == None):
                
                temp = currBT.store[1]
                stk.push(temp)
                tempT = tree.tree(temp.store[0])
                trStk.push(tempT)
                currTree.AddSuccessor(tempT)
                #print(temp.store) 
                while(len((temp.store))>1 and not temp.store[2] == None):
                    #print(temp.store)
                    temp = temp.store[2]
                    
                    tempT = tree.tree(temp.store[0])
                    trStk.push(tempT)
                    currTree.AddSuccessor(tempT)
                    stk.push(temp)
                
