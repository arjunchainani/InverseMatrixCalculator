def MatrixConverter(numVars, equations):

    splitEquation = []
    matrix = []
    resultVector = []
    reversedEquations = []
    reversedResultVector = []
    lenResultVector = []
    

    for i in range(numVars):
        matrix.append([])

    for equation in equations:
        pos = (i - 2)
        for i in range(len(equation)):
            if equation[i] == ' ' and equation[(i - 1)] == 'x':
                while equation[pos] != ' ' and pos >= 0:
                    pass
                            
    
    # for equation in equations:
    #     splitIndivEquation = []
        
    #     for element in equation:
    #         splitIndivEquation.append(element)
        
    #     splitEquation.append(splitIndivEquation)

    # for equation in splitEquation:
    #     for element in equation:
    #         if element == 'x':
    #             if equation.index(element) == 0:
    #                 matrix[splitEquation.index(equation)].append(1)
    #             else: 
    #                 if equation[(equation.index(element) - 1)] == ' ':
    #                     matrix[splitEquation.index(equation)].append(1)
    #                 else:
    #                     matrix[splitEquation.index(equation)].append(int(equation[(equation.index(element) - 1)]))

    #         if element == 'y':
    #             if equation[(equation.index(element) - 1)] == ' ':
    #                 matrix[splitEquation.index(equation)].append(1)
    #             else:
    #                 matrix[splitEquation.index(equation)].append(int(equation[(equation.index(element) - 1)]))  


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

                        
    #         while equation[(-1 * (i + 1))] != ' ':
    #             num.insert(0, equation[(-1 * (i + 1))])
    #             print('In while loop')

    print(resultVector)

    return matrix