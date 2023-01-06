def MatrixVectorProduct(matrix, vector, numVars):
    resultMatrix = []
    for i in range(numVars):
        resultMatrix.append([])
        for j in range(numVars):
            resultMatrix[i].append('')
    
    finalVector = []
 
    for i in range(len(matrix)):
        xPos = 0
        while xPos < numVars:
            resultMatrix[i][xPos] = (float(matrix[i][xPos]) * float(vector[xPos]))
            xPos += 1

    for i in range(numVars):
        finalVector.append([])

    for i in range(len(finalVector)):
        finalVector[i] = sum(resultMatrix[i])

    return finalVector
