from queue import *
from binary_tree import *
from stack import *

class tree:
    def __init__(self,x):
        self.store = [x,[]]

    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True

    def Get_LevelOrder(self):
        que = Queue()
        tStr = []
        que.enqueue(self.store)
        
        while (not(que.isEmpty())):
            temp = que.dequeue()
            name = temp[0]
            tStr = tStr + [name]
            for i in temp[1]:
                que.enqueue(i.store)
        return tStr
    
    def ConvertToBinaryTree(self):
        currTreeQ = Stack()
        currTreeQ.push(self)
        btStack = Stack()
        btHead = binary_tree(self.store[0])
        bt = btHead
        btStack.push(bt)
        while (True):
            #print(btStack.store)
            #print(currTreeQ.store)
            if (currTreeQ.isEmpty()):
                return btHead
            curr = currTreeQ.pop()
            bt = btStack.pop()
            
            #print(curr.store[0])
            #print(curr.store)
            #print(bt.store) 
            head = None
            #print(curr.store[1] == []) 
            if (not curr.store[1] == []):
                head = binary_tree((curr.store[1][0]).store[0])

                #print("Head Val: " + str((head.store[0])))
                #print(head)
                temp = head
                btStack.push(head)
                currTreeQ.push(curr.store[1][0])
                #print(btStack.store)
                for i in range(1,len(curr.store[1])):
                    addNode = binary_tree((curr.store[1][i]).store[0])
                    currTreeQ.push(curr.store[1][i])
                    btStack.push(addNode)
                    temp.AddRight(addNode)
                    temp = addNode
                    
                
                #print(head)
                #print(bt)
                bt.AddLeft(head)
                #print(bt.store)
                #print(btHead) 
            
            #print(len(bt.store))
                

