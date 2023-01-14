import matrix
import invert
import multiplier

numVars = int(input('How many variables are in your system? '));

variables = ['x', 'y', 'z', 'a', 'b', 'c', 'd']

equations = []

for i in range(numVars):
    equations.append(input('Please enter equation #' + str(i + 1) + ' here: '))

resultList = matrix.MatrixConverter(numVars, equations)

origMatrix = resultList[0]
resultVector = resultList[1]

invertedMatrix = invert.matrixInversion(origMatrix, numVars)

finalVector = multiplier.MatrixVectorProduct(invertedMatrix, resultVector, numVars)

for i in range(len(finalVector)):
    finalVector[i] = round(finalVector[i], 2)

for i in range(numVars):
    print('{} = {}'.format(variables[i], finalVector[i]))