def genBoard():
	# 0 -- unoccupied board position
	# 1 -- X occupies the board position
	# 2 -- O occupies the board position
	tBoard = [0,0,0,0,0,0,0,0,0]
	return tBoard

def printBoard(T):
	board = T
	i = 0
	fntWork = True
	if not (len(board) == 9):
		fntWork = False
	while i < len(board):
		currLine = ""
		col = 0
		while col < 3:
			if board[i] == 1:
				currLine = currLine + " X"
			elif board[i] == 2:
				currLine = currLine + " O"
			elif board[i] == 0:
				currLine = currLine + " " + str(i)
			else:
				fntWork = False
			if not (col == 2):
				currLine = currLine + " |"
			col = col + 1
			i = i + 1
		print(currLine)
		if (i < 7):
			print("---|---|---")
	return fntWork

def analyzeBoard(T):
	# 0 -- board is in play
	# 1 -- X won
	# 2 -- O won
	# 3 -- draw
	# Also checks if there are two winners which would be an illegal board	
	board = T
	gameStatus = 0
	fntWork = True
	numX = 0
	numO = 0
	if not (len(board) == 9):
		fntWork = False
	i = 0
	# Check horz win
	while i < len(board):
		if (board[i] == board[i+1] and board[i+1] == board[i+2] and board[i] != 0):	
			if board[i] == 1:
				if gameStatus == 1 or gameStatus == 0:
					gameStatus = 1
				else:
					gameStatus =  -1
			elif board[i] == 2:
				if gameStatus == 2 or gameStatus == 0:
					gameStatus = 2
				else:
					gameStatus = -1
		i = i + 3
	i = 0
	# Check vert win
	while i < 3:
		if (board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] != 0):
			if board[i] == 1:
				if gameStatus == 1 or gameStatus ==0:
					gameStatus = 1
				else:
					gameStatus = -1
			elif board[i] == 2:
				if gameStatus == 2 or gameStatus == 0:
					gameStatus = 2
				else:
					gameStatus = -1
		i = i + 1
	# Check Diag win
	if ((board[0] == board[4] and board[4] == board[8]) or (board[2] == board[4] and board[4] == board[6])):
		if board[4] == 1:
			if gameStatus == 1 or gameStatus == 0:
				gameStatus = 1
			else:
				gameStatus = -1
		elif board[4] == 2:
			if gameStatus == 2 or gameStatus == 0:
				gameStatus = 2
			else:
				gameStatus = -1
	
	i = 0
	#  Check if tie or still in game
	numEmpty = 0
	while i < len(board):
		if board[i] == 1:
			numX = numX + 1
		elif board[i] == 2:
			numO = numO + 1
		if board[i] != 0 and board[i] != 1 and board[i] != 2:
			gameStatus = -1
			break
		elif board[i] == 0:
			if not gameStatus == -1 and not gameStatus == 1 and not gameStatus == 2:
				gameStatus = 0
				numEmpty+=1
		else:
			if not gameStatus == -1 and not gameStatus == 1 and not gameStatus == 2:
				gameStatus = 3
		i = i + 1
	# To make difference possitve, works since has to be a difference of either 0 or 1	
	diff = (numX - numO) * (numX - numO)
	if diff  > 2:
		gameStatus = -1
	
	if not gameStatus == -1 and not gameStatus == 1 and not gameStatus == 2:
		if numEmpty == 0:
			gameStatus = 3
	return gameStatus
		
