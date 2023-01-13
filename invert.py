def Determinant2x2(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

def Determinant3x3(matrix):
    miniOrigMatrix1 = [[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]]
    miniOrigMatrix2 = [[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]]
    miniOrigMatrix3 = [[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]]
    miniDeterminant1 = Determinant2x2(miniOrigMatrix1)
    miniDeterminant2 = Determinant2x2(miniOrigMatrix2)
    miniDeterminant3 = Determinant2x2(miniOrigMatrix3)

    determinant = ((matrix[0][0] * miniDeterminant1) + (-1 * matrix[0][1] * miniDeterminant2) + (matrix[0][2] * miniDeterminant3))

    return determinant

def matrixInversion(matrix, numVars):

    if numVars == 2:
        firstInvertedMatrix = [[0, 0], [0, 0]]
        firstInvertedMatrix[0][0] = matrix[1][1]
        firstInvertedMatrix[1][1] = matrix[0][0]
        firstInvertedMatrix[0][1] = (matrix[0][1] * -1)
        firstInvertedMatrix[1][0] = (matrix[1][0] * -1)

        determinant = Determinant2x2(matrix)

        invertedMatrix = [[0, 0], [0, 0]]

        for i in range(len(firstInvertedMatrix)):
            for j in range(len(firstInvertedMatrix[i])):
                try:
                    invertedMatrix[i][j] = (firstInvertedMatrix[i][j] / determinant)
                except:
                    pass

        if determinant != 0:
            return invertedMatrix
        else:
            return 'No solution'

    if numVars == 3:
        determinant = Determinant3x3(matrix)    

        transposedMatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        transposedMatrix[0][0] = matrix[0][0]
        transposedMatrix[0][1] = matrix[1][0]
        transposedMatrix[0][2] = matrix[2][0]
        transposedMatrix[1][0] = matrix[0][1]
        transposedMatrix[1][1] = matrix[1][1]
        transposedMatrix[1][2] = matrix[2][1]
        transposedMatrix[2][0] = matrix[0][2]
        transposedMatrix[2][1] = matrix[1][2]
        transposedMatrix[2][2] = matrix[2][2]

        adjunctMatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        minorMatrix1 = [[transposedMatrix[1][1], transposedMatrix[1][2]], [transposedMatrix[2][1], transposedMatrix[2][2]]]
        minorMatrix2 = [[transposedMatrix[1][0], transposedMatrix[1][2]], [transposedMatrix[2][0], transposedMatrix[2][2]]]
        minorMatrix3 = [[transposedMatrix[1][0], transposedMatrix[1][1]], [transposedMatrix[2][0], transposedMatrix[2][1]]]
        minorMatrix4 = [[transposedMatrix[0][1], transposedMatrix[0][2]], [transposedMatrix[2][1], transposedMatrix[2][2]]]
        minorMatrix5 = [[transposedMatrix[0][0], transposedMatrix[0][2]], [transposedMatrix[2][0], transposedMatrix[2][2]]]
        minorMatrix6 = [[transposedMatrix[0][0], transposedMatrix[0][1]], [transposedMatrix[2][0], transposedMatrix[2][1]]]
        minorMatrix7 = [[transposedMatrix[0][1], transposedMatrix[0][2]], [transposedMatrix[1][1], transposedMatrix[1][2]]]
        minorMatrix8 = [[transposedMatrix[0][0], transposedMatrix[0][2]], [transposedMatrix[1][0], transposedMatrix[1][2]]]
        minorMatrix9 = [[transposedMatrix[0][0], transposedMatrix[0][1]], [transposedMatrix[1][0], transposedMatrix[1][1]]]
        adjunctMatrix[0][0] = Determinant2x2(minorMatrix1)
        adjunctMatrix[0][1] = Determinant2x2(minorMatrix2)
        adjunctMatrix[0][2] = Determinant2x2(minorMatrix3)
        adjunctMatrix[1][0] = Determinant2x2(minorMatrix4)
        adjunctMatrix[1][1] = Determinant2x2(minorMatrix5)
        adjunctMatrix[1][2] = Determinant2x2(minorMatrix6)
        adjunctMatrix[2][0] = Determinant2x2(minorMatrix7)
        adjunctMatrix[2][1] = Determinant2x2(minorMatrix8)
        adjunctMatrix[2][2] = Determinant2x2(minorMatrix9)

        for i in range(len(adjunctMatrix)):
            for j in range(len(adjunctMatrix[i])):
                if i == 1:
                    if j % 2 == 0:
                        adjunctMatrix[i][j] = (-1 * adjunctMatrix[i][j])
                    else:
                        pass
                else:
                    if j % 2 != 0:
                        adjunctMatrix[i][j] = (-1 * adjunctMatrix[i][j])
                    else:
                        pass

        inverseMatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(adjunctMatrix)):
            for j in range(len(adjunctMatrix[i])):
                inverseMatrix[i][j] = (adjunctMatrix[i][j] / determinant)

        if (determinant != 0): 
            return inverseMatrix
        else:
            return 'No solution'
        
