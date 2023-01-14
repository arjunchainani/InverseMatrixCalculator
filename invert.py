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

def Determinant4x4(matrix):
  cofactorMatrix1 = [[matrix[1][1], matrix[1][2], matrix[1][3]], [matrix[2][1], matrix[2][2], matrix[2][3]], [matrix[3][1], matrix[3][2], matrix[3][3]]]
  cofactorMatrix2 = [[matrix[0][1], matrix[0][2], matrix[0][3]], [matrix[2][1], matrix[2][2], matrix[2][3]], [matrix[3][1], matrix[3][2], matrix[3][3]]]
  cofactorMatrix3 = [[matrix[0][1], matrix[0][2], matrix[0][3]], [matrix[1][1], matrix[1][2], matrix[1][3]], [matrix[3][1], matrix[3][2], matrix[3][3]]]
  cofactorMatrix4 = [[matrix[0][1], matrix[0][2], matrix[0][3]], [matrix[1][1], matrix[1][2], matrix[1][3]], [matrix[2][1], matrix[2][2], matrix[2][3]]]
  cofactorDeterminant1 = Determinant3x3(cofactorMatrix1)
  cofactorDeterminant2 = Determinant3x3(cofactorMatrix2)
  cofactorDeterminant3 = Determinant3x3(cofactorMatrix3)
  cofactorDeterminant4 = Determinant3x3(cofactorMatrix4)

  determinant = (matrix[0][0] * cofactorDeterminant1) - (matrix[1][0] * cofactorDeterminant2) + (matrix[2][0] * cofactorDeterminant3) - (matrix[3][0] * cofactorDeterminant4)

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

    if numVars == 4:
        determinant = Determinant4x4(matrix)

        minorMatrix1 = [[matrix[1][1], matrix[1][2], matrix[1][3]], [matrix[2][1], matrix[2][2], matrix[2][3]], [matrix[3][1], matrix[3][2], matrix[3][3]]]
        minorMatrix2 = [[matrix[1][0], matrix[1][2], matrix[1][3]], [matrix[2][0], matrix[2][2], matrix[2][3]], [matrix[3][0], matrix[3][2], matrix[3][3]]]
        minorMatrix3 = [[matrix[1][0], matrix[1][1], matrix[1][3]], [matrix[2][0], matrix[2][1], matrix[2][3]], [matrix[3][0], matrix[3][1], matrix[3][3]]]
        minorMatrix4 = [[matrix[1][0], matrix[1][1], matrix[1][2]],[matrix[2][0], matrix[2][1], matrix[2][2]], [matrix[3][0], matrix[3][1], matrix[3][2]]]
        minorMatrix5 = [[matrix[0][1], matrix[0][2], matrix[0][3]], [matrix[2][1], matrix[2][2], matrix[2][3]], [matrix[3][1], matrix[3][2], matrix[3][3]]]
        minorMatrix6 = [[matrix[0][0], matrix[0][2], matrix[0][3]], [matrix[2][0], matrix[2][2], matrix[2][3]], [matrix[3][0], matrix[3][2], matrix[3][3]]]
        minorMatrix7 = [[matrix[0][0], matrix[0][1], matrix[0][3]], [matrix[2][0], matrix[2][1], matrix[2][3]], [matrix[3][0], matrix[3][1], matrix[3][3]]]
        minorMatrix8 = [[matrix[0][0], matrix[0][1], matrix[0][2]], [matrix[2][0], matrix[2][1], matrix[2][2]], [matrix[3][0], matrix[3][1], matrix[3][2]]]
        minorMatrix9 = [[matrix[0][1], matrix[0][2], matrix[0][3]], [matrix[1][1], matrix[1][2], matrix[1][3]], [matrix[3][1], matrix[3][2], matrix[3][3]]]
        minorMatrix10 = [[matrix[0][0], matrix[0][2], matrix[0][3]], [matrix[1][0], matrix[1][2], matrix[1][3]], [matrix[3][0], matrix[3][2], matrix[3][3]]]
        minorMatrix11 = [[matrix[0][0], matrix[0][1], matrix[0][3]], [matrix[1][0], matrix[1][1], matrix[1][3]], [matrix[3][0], matrix[3][1], matrix[3][3]]]
        minorMatrix12 = [[matrix[0][0], matrix[0][1], matrix[0][2]], [matrix[1][0], matrix[1][1], matrix[1][2]], [matrix[3][0], matrix[3][1], matrix[3][2]]]
        minorMatrix13 = [[matrix[0][1], matrix[0][2], matrix[0][3]], [matrix[1][1], matrix[1][2], matrix[1][3]], [matrix[2][1], matrix[2][2], matrix[2][3]]]
        minorMatrix14 = [[matrix[0][0], matrix[0][2], matrix[0][3]], [matrix[1][0], matrix[1][2], matrix[1][3]], [matrix[2][0], matrix[2][2], matrix[2][3]]]
        minorMatrix15 = [[matrix[0][0], matrix[0][1], matrix[0][3]], [matrix[1][0], matrix[1][1], matrix[1][3]], [matrix[2][0], matrix[2][1], matrix[2][3]]]
        minorMatrix16 = [[matrix[0][0], matrix[0][1], matrix[0][2]], [matrix[1][0], matrix[1][1], matrix[1][2]], [matrix[2][0], matrix[2][1], matrix[2][2]]]

        adjunctMatrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        adjunctMatrix[0][0] = Determinant3x3(minorMatrix1)
        adjunctMatrix[0][1] = Determinant3x3(minorMatrix2)
        adjunctMatrix[0][2] = Determinant3x3(minorMatrix3)
        adjunctMatrix[0][3] = Determinant3x3(minorMatrix4)
        adjunctMatrix[1][0] = Determinant3x3(minorMatrix5)
        adjunctMatrix[1][1] = Determinant3x3(minorMatrix6)
        adjunctMatrix[1][2] = Determinant3x3(minorMatrix7)
        adjunctMatrix[1][3] = Determinant3x3(minorMatrix8)
        adjunctMatrix[2][0] = Determinant3x3(minorMatrix9)
        adjunctMatrix[2][1] = Determinant3x3(minorMatrix10)
        adjunctMatrix[2][2] = Determinant3x3(minorMatrix11)
        adjunctMatrix[2][3] = Determinant3x3(minorMatrix12)
        adjunctMatrix[3][0] = Determinant3x3(minorMatrix13)
        adjunctMatrix[3][1] = Determinant3x3(minorMatrix14)
        adjunctMatrix[3][2] = Determinant3x3(minorMatrix15)
        adjunctMatrix[3][3] = Determinant3x3(minorMatrix16)

        for i in range(len(adjunctMatrix)):
            for j in range(len(adjunctMatrix[i])):
                if i % 2 == 0:
                    if j % 2 != 0:
                        adjunctMatrix[i][j] = (-1 * adjunctMatrix[i][j])
                else:
                    if j % 2 == 0:
                        adjunctMatrix[i][j] = (-1 * adjunctMatrix[i][j])

        inverseMatrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        for i in range(len(adjunctMatrix)):
            for j in range(len(adjunctMatrix[i])):
                inverseMatrix[i][j] = (adjunctMatrix[i][j] / determinant)

        transposedInverseMatrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(len(inverseMatrix)):
            for j in range(len(inverseMatrix[i])):
                transposedInverseMatrix[j][i] = inverseMatrix[i][j]

        return transposedInverseMatrix

            
