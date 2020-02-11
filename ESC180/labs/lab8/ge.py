def ge_fw(mat):
    matrix = mat
    overallMatrix = mat
    rowCount  = 0

    while(True):

        for i in range(0,len(matrix),1):
            if (matrix[i][0] != 0 and matrix[0][0] == 0):
                temp = list(matrix[0])
                matrix[0] = list(matrix[i])
                matrix[i] = temp
                overallMatrix[rowCount] =[0]*rowCount+ list(matrix[0])
                rowCount += 1
                break
        for i in range(1,len(matrix),1):
            if (matrix[i][0] != 0):
                factor = matrix[i][0] / matrix[0][0]
                for j in range(0,len(matrix[i]),1):
                    matrix[i][j] = matrix[i][j] + -1 * factor * matrix[0][j]

        temp = [[0]*(len(matrix[0])-1)] * (len(matrix)-1)
        countR = 0
        for i in range(1,len(matrix),1):
            countC = 0
            for j in range(1,len(matrix[i]),1):
                temp[countR][countC] = matrix[i][j]
                countC += 1
            countR += 1
        #print(overallMatrix)
        if len(matrix) <= 1 or len(matrix[0]) <= 1:
            break
        else:
            matrix = list(temp)

    return overallMatrix



def ge_bw(mat):
    matrix = mat
    overallMatrix = mat
    rowCount = len(mat)-1
    while(True):
        ind = 0
        for i in matrix[len(matrix)-1]:
            if i != 0:
                fact = i
                break
            ind += 1
        if (ind >= len(matrix[len(matrix)-1])):
                ind =0 
        for i in range(0,len(matrix[0]),1):
            if(matrix[len(matrix)-1][i] == 1):
                break
            else:
                matrix[len(matrix)-1][i] = matrix[len(matrix)-1][i] / fact

        overallMatrix[rowCount] =list(matrix[rowCount])
        rowCount -= 1

        #print(matrix)
        for i in range(0,len(matrix)-1,1):
            #print(matrix)
            multFact = matrix[i][ind]
            for j in range(0,len(matrix[i]),1):
                #print(matrix[i][j])
                matrix[i][j] = matrix[i][j]+ -1* matrix[len(matrix)-1][j]*multFact
                #print(matrix[len(matrix)-2][len(matrix[0])-1])
        temp = [[0]*(len(matrix[0])) for x in range (len(matrix)-1)]
        countR = 0
        #print(temp)
        for i in range(0,len(matrix)-1,1):
            countC = 0

            for j in range(0,len(matrix[i]),1):
                #print(temp)

                temp[countR][countC] = matrix[i][j]
                countC += 1
            #print(temp)
            countR += 1
        #print(matrix)
        #print(temp)
        if rowCount < 0 or len(matrix) <= 0 or len(matrix[0]) <= 0:
            #print(overallMatrix)
            break
        else:
            matrix = list(temp)
            #print(overallMatrix)

    return overallMatrix

