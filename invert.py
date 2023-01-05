def matrixInversion(matrix, numVars):
 
  if numVars == 2:
    firstInvertedMatrix = [[0, 0], [0, 0]]
    firstInvertedMatrix[0][0] = matrix[1][1]
    firstInvertedMatrix[1][1] = matrix[0][0]
    firstInvertedMatrix[0][1] = (matrix[0][1] * -1)
    firstInvertedMatrix[1][0] = (matrix[1][0] * -1)

    determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
   
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

matrixInverted = matrixInversion([[1, 1], [1, 1]], 2)
print(matrixInverted)