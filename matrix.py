def MatrixConverter(numVars, equations):

    splitEquation = []
    matrix = []
    resultVector = []
    indivResult = []

    for i in range(numVars):
        matrix.append([])

    for equation in equations:
        splitIndivEquation = []
        
        for element in equation:
            splitIndivEquation.append(element)
        
        splitEquation.append(splitIndivEquation)

    for equation in splitEquation:
        for element in equation:
            if element == 'x':
                if equation.index(element) == 0:
                    matrix[splitEquation.index(equation)].append(1)
                else: 
                    if equation[(equation.index(element) - 1)] == ' ':
                        matrix[splitEquation.index(equation)].append(1)
                    else:
                        matrix[splitEquation.index(equation)].append(int(equation[(equation.index(element) - 1)]))

            if element == 'y':
                if equation[(equation.index(element) - 1)] == ' ':
                    matrix[splitEquation.index(equation)].append(1)
                else:
                    matrix[splitEquation.index(equation)].append(int(equation[(equation.index(element) - 1)]))  

    for equation in splitEquation:
        num = []
        for i in range(len(equation)):
            while equation[(-1 * (i + 1))] != ' ':
                num.insert(0, equation[(-1 * (i + 1))])
                      
    print(num)

    return matrix