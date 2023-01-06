import matrix

numVars = int(input('How many variables are in your system? '));

equations = []

for i in range(numVars):
    equations.append(input('Please enter equation #' + str(i + 1) + ' here: '))

resultList = matrix.MatrixConverter(numVars, equations)

origMatrix = resultList[0]
resultVector = resultList[1]
print(origMatrix)
print(resultVector)