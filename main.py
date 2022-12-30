import matrix

numVars = int(input('How many variables are in your system? '));

equations = []

for i in range(numVars):
    equations.append(input('Please enter the equation #' + str(i + 1) + ' here: '))

origMatrix = matrix.MatrixConverter(numVars, equations)
print(origMatrix)