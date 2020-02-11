teOffset = 10
blackOffset = 20
pawnVal = 0
knightVal = 1
bishopVal = 2
rookVal  = 3
queenVal = 4
kingVal = 5
#bellow is the list of each row and the index values
rowOne= [0,1,2,3,4,5,6,7]
rowTwo= [8,9,10,11,12,13,14,15]
rowThree= [16,17,18,19,20,21,22,23]
rowFour=[24,25,26,27,28,29,30,31]
rowFive= [32,33,34,35,36,37,38,39]
rowSix= [40,41,42,43,44,45,46,47]
rowSeven= [48,49,50,51,52,53,54,55]
rowEight= [56,57,58,59,60,61,62,63]

rows = [rowOne,rowTwo,rowThree,rowFour,rowFive,rowSix,rowSeven,rowEight]
"""TODO TESTING TO SEE IF ALGO WORKS"""
class Tree():
    def __init__(self,boardState):
        self.boardState = boardState
        self.children = []
        #change in val for this state
        self.val = 0
    def addChild(self,child):
        self.children += [child]

class queue():
    def __init__(self):
        self.store = []
    def enqueue(self,val):
        self.store = self.store + [val]
        return 1
    def dequeue(self):
        temp = self.store[len(self.store)-1]
        self.store = self.store[0:len(self.store)-1]
        return temp
 
def initGame():
        boardInit = [13,11,12,14,15,12,11,13,10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,20,20,20,20,20,20,23,21,22,24,25,22,21,23]
      
#returns the index of which row
def getRow(index):
    return (int)(index/8)

#determine if in same row
def isInSameRow(i,j):
    if getRow(i) == getRow(j):
            return True
    else:
        return False
  
def GetPlayerPositions(board,player):
    moves=[]
    i=0
    for i in range(0,64):
        if board[i] >= player and board[i] < player+10:
            moves += [i]
    return moves

#NEED TO FIND WAY THAT DOES PUT KING IN CHECK
def GetPieceLegalMoves(board,pos):
    moves = []
    #0 for white, 1 for black
    currPlayer = -1
    if (board[pos] < 20):
        currPlayer = 0
    else:
        currPlayer = 1
      
  
    #will have error on edge cases
    if board[pos]  == whiteOffset + pawnVal:
        if (pos+8) < 64 and board[pos+8] == 0:
            moves += [pos+8]
        #Modding by 8 to find if edge case
        if (pos+9 < 64 and (pos+1)%8 > 0):
           if board[pos+9] >= 20:
               moves += [pos+9]
        if board[pos+7] >= 20 and (pos)%8 > 0:
                    moves += [pos+7]
  
    if board[pos]  == blackOffset + pawnVal:
        if (pos-8) > 0 and board[pos+8] == 0:
            moves += [pos-8]
        #Modding by 8 to find if edge case
        if (pos-9 > 0 and (pos)%8 > 0):
            if board[pos-9] < 20:
                    moves += [pos-9]
        if board[pos-7] < 20 and (pos+1)%8 > 0:
                    moves += [pos-7]
  
    #KNIGHT MOVES TODO REDUCE SIZE OF THIS SECTION
    if board[pos]  == whiteOffset + knightVal or board[pos]  == blackOffset + knightVal:
        #8 cases for a knight
        if (pos+15 < 64 and isInSameRow(pos+16,pos+15)):
            if currPlayer == 0:
                if board[pos+15] >= 20 or board[pos+15] == 0:
                    moves += [pos+15]
            if currPlayer == 1:
                if board[pos+15] < 20 or board[pos+15] == 0:
                    moves += [pos+15]
      
        if (pos+17 < 64 and isInSameRow(pos+16,pos+17)):
            if currPlayer == 0:
                if board[pos+17] >= 20 or board[pos+17] == 0:
                    moves += [pos+17]
            if currPlayer == 1:
                if board[pos+17] < 20 or board[pos+17] == 0:
                    moves += [pos+17]
     
        if (pos+10 < 64 and isInSameRow(pos+8,pos+10)):
            if currPlayer == 0:
                if board[pos+10] >= 20 or board[pos+10] == 0:
                    moves += [pos+10]
            if currPlayer == 1:
                if board[pos+10] < 20 or board[pos+10] == 0:
                    moves += [pos+10]
      
        if (pos-6 >0 and isInSameRow(pos-8,pos-6)):
            if currPlayer == 0:
                if board[pos-6] >= 20 or board[pos-6] == 0:
                    moves += [pos-6]
            if currPlayer == 1:
                if board[pos-6] < 20 or board[pos-6] == 0:
                    moves += [pos-6]   
                  
        if (pos+6 < 64  and isInSameRow(pos+8,pos+6)):
            if currPlayer == 0:
                if board[pos+6] >= 20 or board[pos+6] == 0:
                    moves += [pos+6]
            if currPlayer == 1:
                if board[pos+6] < 20 or board[pos+6] == 0:
                    moves += [pos+6]
      
        if (pos-10 > 0 and isInSameRow(pos-8,pos-10)):
            if currPlayer == 0:
                if board[pos-10] >= 20 or board[pos-10] == 0:
                    moves += [pos-10]
            if currPlayer == 1:
                if board[pos-10] < 20 or board[pos-10] == 0:
                    moves += [pos-10]
                  
        if (pos-15 > 0  and isInSameRow(pos-16,pos-15)):
            if currPlayer == 0:
                if board[pos-15] >= 20 or board[pos-15] == 0:
                    moves += [pos-15]
            if currPlayer == 1:
                if board[pos-15] < 20 or board[pos-15] == 0:
                    moves += [pos-15]
  
        if (pos-17 > 0 and isInSameRow(pos-16,pos-17)):
            if currPlayer == 0:
                if board[pos-17] >= 20 or board[pos-17] == 0:
                    moves += [pos-17]
            if currPlayer == 1:
                if board[pos-17] < 20 or board[pos-17] == 0:
                    moves += [pos-17]
                  
     #Vertical and Horz Moves
    if board[pos]  == whiteOffset + rookVal or board[pos]  == blackOffset + rookVal or board[pos]  == whiteOffset + queenVal or board[pos]  == blackOffset + queenVal:
         #Vert Moves
         if(pos+8 < 64):
             moves = checkCol(currPlayer,moves,pos+8,64,8,board)
         if(pos-8 > 0):
             moves = checkCol(currPlayer,moves,pos-8,0,-8,board)
        #Horz Moves
         tempRow = rows[getRow(pos)]
         if(pos+1 < 64):
                 moves = checkCol(currPlayer,moves,pos+1,tempRow[7],1,board)
         if(pos-1 > 0):
                 moves = checkCol(currPlayer,moves,pos-1,tempRow[0],-1,board)
   
    #Diag Moves                     
    if board[pos]  == whiteOffset + bishopVal or board[pos]  == blackOffset + bishopVal or board[pos]  == whiteOffset + queenVal or board[pos]  == blackOffset + queenVal:
        if (pos+9 < 64):
            moves = checkCol(currPlayer,moves,pos+9,64,9,board)
        if (pos+7 < 64):
            moves = checkCol(currPlayer,moves,pos+7,64,7,board)
        if(pos-9>0):
            moves = checkCol(currPlayer,moves,pos-9,0,-9,board)
        if(pos-7>0):
            moves = checkCol(currPlayer,moves,pos-7,0,-7,board)
  
    #King Moves
    if board[pos]  == whiteOffset + kingVal or board[pos]  == blackOffset + kingVal:
        if (pos+9 < 64):
            moves = checkCol(currPlayer,moves,pos+9,pos+18,9,board)
        if (pos+7 < 64):
            moves = checkCol(currPlayer,moves,pos+7,pos+14,7,board)
        if(pos-9>0):
            moves = checkCol(currPlayer,moves,pos-9,pos-18,-9,board)
        if(pos-7>0):
            moves = checkCol(currPlayer,moves,pos-7,pos-14,-7,board)         
        #Vert Moves
        if(pos+8 < 64):
             moves = checkCol(currPlayer,moves,pos+8,pos+16,8,board)
        if(pos-8 > 0):
             moves = checkCol(currPlayer,moves,pos-8,pos-16,-8,board)
        #Horz Moves
        tempRow = rows[getRow(pos)]
        if(pos+1 < 64):
                 moves = checkCol(currPlayer,moves,pos+1,min(pos+2,tempRow[7]),1,board)
        if(pos-1 > 0):
                 moves = checkCol(currPlayer,moves,pos-1,min(pos-2,tempRow[0]),-1,board)
      
    return moves
          
def IsPositionUnderThreat(board,position,player):
    if player == 0:
        for i in range(0,64):
            if board[i] >= 19:
                temp = GetPieceLegalMoves(board,i)
                if position in temp:
                    return True
    if player == 1:
        for i in range(0,64):
            if board[i] > 0 and board[i] < 20:
                temp = GetPieceLegalMoves(board,i)
                if position in temp:
                    return True


def checkCol(currPlayer,moves,start,bound,inc,board):
    for i in range(start,bound,inc):
        if currPlayer == 0:
            if board[i] >= 20:
                moves += [i]
                break
            elif board[i] == 0:
                moves += [i]
            elif board[i] < 20:
                break
        if currPlayer == 1:
            if board[i] >= 20:
                break
            elif board[i] == 0:
                moves += [i]
            elif board[i] < 20:
                moves+=[i]
                break
    return moves
#find the potential moves and store the board state with each these potential moves
#Right now checks all potential moves and reactions to find what is the most viable moves
def pickMove (currPlayer,board):
    optTree = Tree(board)
    optTree.val = assessBoard(board)
    addChildren(currPlayer, board, optTree)
    if currPlayer == 0:
        for i in optTree.children:
            addChildren(1,i.boardState,i)
    elif currPlayer == 1:
        for i in optTree.children:
            addChildren(0,i.boardState,i)
   
    #apply min-max algo (or max-min if for black)
    tempArr = []
    maxI = -1
    canidates = []
    currMove = []
    if currPlayer==0:
        for i in optTree.children:
            tempArr += [getMins(optTree)]
        #need to do loop like this to get index
        tempMax = -100000000
        for i in range(0,len(tempArr)):           
            currMove = currMove + [getMoveChange(board,optTree,i)]
            if tempArr[i] > tempMax:
                tempMax = tempArr[i]
                maxI = i
   
    if currPlayer==1:
        for i in optTree.children:
            tempArr += [getMaxs(optTree)]
        #need to do loop like this to get index
        tempMin = 100000000
        for i in range(0,len(tempArr)):
            
            currMove = currMove + [getMoveChange(board,optTree,i)]
            if tempArr[i] < tempMin:
                tempMin = tempArr[i]
                maxI = i
    
    return [(optTree.children[maxI]).boardState, getMoveChange(board,optTree,maxI), currMove, optTree]

def getMoveChange(board,tree,index):
    temp = []
    for i in range(0,64):
        if not board[i] == tree.children[index].boardState[i] and board[i] == 0:
            temp = temp + [i]
        elif not board[i] == tree.children[index].boardState[i] and tree.children[index].boardState[i] == 0:
            temp = [i] + temp
    temp = [temp] + [tree.children[index].val]
    return temp

def getMins(tree):
    temp = []
    for i in tree.children:
        temp += [i.val]
    return min(temp)

def getMaxs(tree):
    temp = []
    for i in tree.children:
        temp += [i.val]
    return max(temp)

def addChildren(currPlayer, board,pTree):
    if currPlayer == 0:
        for i in range(0,64):
            if board[i] > 0 and board[i] < 20:
                posMoves = GetPieceLegalMoves(board,i)
                #now create the board for each potential move and add as child to tree
                for j in posMoves:
                    tempBoard = list(board)
                    tempBoard[i] = 0
                    tempBoard[j] = board[i]
                    tempTree = Tree(tempBoard)
                    tempTree.val = assessBoard(tempTree.boardState)
                    pTree.addChild(tempTree)
    if currPlayer == 1:
        for i in range(0,64):
            if board[i] > 19:
                posMoves = GetPieceLegalMoves(board,i)
                #now create the board for each potential move and add as child to tree
                for j in posMoves:
                    tempBoard = list(board)
                    tempBoard[i] = 0
                    tempBoard[j] = board[i]
                    tempTree = Tree(tempBoard)
                    tempTree.val = assessBoard(tempTree.boardState)
                    pTree.addChild(tempTree)
   

#determine the value of the board
#POS vals favourable for white
#NEG vals favourable for black
def assessBoard(board):
    kingCVal = 100000
    queenCVal = 9
    rookCVal = 5
    bishopCVal = 3
    knightCVal = 3
    pawnCVal = 1
    val = 0
   
    for i in board:
        if i == whiteOffset + pawnVal:
            val += pawnCVal
        elif i == blackOffset + pawnVal:
            val -= pawnCVal
           
        elif i == whiteOffset + knightVal:
            val += knightCVal
        elif i == blackOffset + knightVal:
            val -= knightCVal
           
        elif i == whiteOffset + bishopVal:
            val += bishopCVal
        elif i == blackOffset + bishopVal:
            val -= bishopCVal
           
        elif i == whiteOffset + rookVal:
            val += rookCVal
        elif i == blackOffset + rookVal:
            val -= rookCVal
           
        elif i == whiteOffset + queenVal:
            val += queenCVal
        elif i == blackOffset + queenVal:
            val -= queenCVal
           
        elif i == whiteOffset + kingVal:
            val += kingCVal
        elif i == blackOffset + kingVal:
            val -= kingCVal
           
    return val
   
#boardInit = [13,11,12,14,15,12,11,13,10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,20,20,20,20,20,20,23,21,22,24,25,22,21,23]

#print (GetPlayerPositions(boardInit,10))


#print (GetPieceLegalMoves(boardInit,47))

def printBoard(board):
    overall = []
    temp = []
    for i in range(0,64):
        temp += [board[i]]
        if (i+1) % 8 == 0 and i > 0:
            overall = [temp] + overall
            temp = []
    for i in overall:
        print (i)

def chessPlayer(board, player):
    temp = pickMove(player, board)
    return [True, temp[1], temp[2], getLevelOrder(temp[3],board)]


def getLevelOrder(tree,board):
    x = queue()
    x.enqueue(tree)
    temp = []
    while (len(x.store) > 0):
        tempT = x.dequeue()
        for i in tempT.children:
            x.enqueue(i)
        temp = temp + [[getBoardDiff(board,tempT.boardState),tempT.val]]
    return temp

def getBoardDiff(board0, board1):
    temp = []
    for i in range(0,64):
        if not board0[i] == board1[i] and board1[i] == 0:
            temp = temp + [i]
        elif not board1[i] == board1[i] and board1[i] == 0:
            temp = [i] + temp
        if (len(temp) == 2):
            break
    return temp
#printBoard(boardInit)
