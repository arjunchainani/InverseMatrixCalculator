def MatrixConverter(numVars, equations):

    splitEquation = []
    matrix = [[], []]

    for equation in equations:
        splitIndivEquation = []
        
        for element in equation:
            splitIndivEquation.append(element)
        
        splitEquation.append(splitIndivEquation)

    print(splitEquation)

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

    return matrix