def MatrixConverter(numVars, equations):

    splitEquation = []
    matrix = []
    resultVector = []
    reversedEquations = []
    reversedResultVector = []
    lenResultVector = []
    

    for i in range(numVars):
        matrix.append([])
        for j in range(numVars):
            matrix[i].append('')

    for numEquation in range(len(equations)):
        num = ''
        for i in range(len(equations[numEquation])):
            pos = (i - 2)
            if equations[numEquation][i] == ' ' and equations[numEquation][(i - 1)] == 'x':
                while equations[numEquation][pos] != ' ' and pos >= 0:
                    num += equations[numEquation][pos]
                    pos -= 1

                if num == '':
                    matrix[numEquation][0] = 1
                elif num == '-':
                    matrix[numEquation][0] = -1
                else:
                    matrix[numEquation][0] = int(num[::-1])

            num = ''
            if equations[numEquation][i] == ' ' and equations[numEquation][(i - 1)] == 'y':
                while equations[numEquation][pos] != ' ' and pos >= 0:
                    num += equations[numEquation][pos]
                    pos -= 1

                if num != '':
                    matrix[numEquation][1] = int(num[::-1])
                else:
                    matrix[numEquation][1] = 1

            num = ''
            if equations[numEquation][i] == ' ' and equations[numEquation][(i - 1)] == 'z':
                while equations[numEquation][pos] != ' ' and pos >= 0:
                    num += equations[numEquation][pos]
                    pos -= 1

                if num != '':
                    matrix[numEquation][2] = int(num[::-1])
                else:
                    matrix[numEquation][2] = 1

            num = ''
            if equations[numEquation][i] == ' ' and equations[numEquation][(i - 1)] == 'a':
                while equations[numEquation][pos] != ' ' and pos >= 0:
                    num += equations[numEquation][pos]
                    pos -= 1

                if num != '':
                    matrix[numEquation][3] = int(num[::-1])
                else:
                    matrix[numEquation][3] = 1

            num = ''
            if equations[numEquation][i] == ' ' and equations[numEquation][(i - 1)] == 'b':
                while equations[numEquation][pos] != ' ' and pos >= 0:
                    num += equations[numEquation][pos]
                    pos -= 1

                if num != '':
                    matrix[numEquation][4] = int(num[::-1])
                else:
                    matrix[numEquation][4] = 1

            num = ''
            if equations[numEquation][i] == ' ' and equations[numEquation][(i - 1)] == 'c':
                while equations[numEquation][pos] != ' ' and pos >= 0:
                    num += equations[numEquation][pos]
                    pos -= 1

                if num != '':
                    matrix[numEquation][5] = int(num[::-1])
                else:
                    matrix[numEquation][5] = 1

            num = ''
            if equations[numEquation][i] == ' ' and equations[numEquation][(i - 1)] == 'd':
                while equations[numEquation][pos] != ' ' and pos >= 0:
                    num += equations[numEquation][pos]
                    pos -= 1

                if num != '':
                    matrix[numEquation][6] = int(num[::-1])
                else:
                    matrix[numEquation][6] = 1


    for equation in equations:
        reversedEquations.append(equation[::-1])

    for i in range(len(reversedEquations)):
        for j in range(len(reversedEquations[i])):
            if reversedEquations[i][j] == ' ':
                lenResultVector.append(j)
                break

    for i in range(len(reversedEquations)):
        reversedResultVector.append(reversedEquations[i][:(lenResultVector[i])])

    for vector in reversedResultVector:
        resultVector.append(int(vector[::-1]))

    return [matrix, resultVector]