from tttlib import *

x = genBoard()

testCases = [
	[1,2,1,2,1,2,0,2,1],
	[1,2,0,2,1,0,2,0,1],
	[1,1,1,1,1,1,1,1,1,1,1,1],
	[2,1,0,1,2,0,1,0,2],
	[1,1,1,2,1,2,0,2,0],
	[2,2,2,1,1,1,1,2,1],
	[1,2,1,2,1,1,2,1,2],
	[2,2,2,1,1,2,1,1,2],
	[0,0,0,0,0,0,0,0,0],
	[1,2,1,2,1,2,0,2,1],
	[1,0,2,1,2,1,2,2,1],
	[1,0,0,0,0,1,2,2,2],
	[1,0,0,2,2,2,1,0,0],
	[0,1,2,1,2,0,2,1,0],
	[0,2,1,2,0,1,2,0,1],
	[1,1,2,0,1,0,2,0,0],
	[0,0,0,0,0,0,0,2,0]
	]

# itterate through the test cases
for i in testCases:
	print("board status: " + str(printBoard(i)))
	print("AnalyzeBoard: " + str(analyzeBoard(i)))

print("\n<------Switch Xs and Os-------->\n")
# invert the test cases then chec
for i in testCases:
	tempLs = []
	for j in i:
		if j == 1:
			tempLs = tempLs + [2]
		elif j == 2:
			tempLs = tempLs + [1]
		else:
			tempLs = tempLs + [0]
	print("board status: " + str(printBoard(tempLs)))
	print("AnalyzeBoard: " + str(analyzeBoard(tempLs)))

