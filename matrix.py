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
        print('Len: ' + str(len(equation)))   
        for i in range(1, len(equation)):
            num = []
            print(equation[-1 * (i + 1)])
            if equation[-1 * (i + 1)] == ' ' and i != 1:
                # num.append(equation[(-1 * (i - 1))])
                # num.insert(0, str(equation[(-1 * i)]))
                num.append(equation[(-1 * i)])
                print('If statement 1 for ' + equation[(-1 * i)])
                break
            elif equation[-1 * (i + 1)] == ' ' and i == 1:
                # num.insert(0, str(equation[(-1 * i)]))
                num.append(equation[(-1 * i)])
                print('If statement 2 for ' + equation[(-1 * i)])
                break
            else:
                if i == 1:
                    # num.insert(0, str(equation[(-1 * i)])) 
                    num.append(equation[(-1 * i)])
                    print('If statement 3 for ' + equation[(-1 * i)])
                else: 
                    # num.append(equation[(-1 * (i - 1))])
                    # num.insert(0, str(equation[(-1 * i)])) 
                    num.append(equation[(-1 * i)])

                    print('If statement 4 for ' + equation[(-1 * i)])

        # for i in range(1, len(equation)):
        #     num = []
        #     if equation[-1 * (i + 1)] != ' ':
        #         num = [equation[-1 * i]] + num
        #     elif equation[-1 * (i + 1)] == ' ':
        #         num = [equation[-1 * i]] + num
        #     else:
        #         print('Error creating result vector')
        finalNum = num.reverse()

        resultVector.append(finalNum)
                
    #         while equation[(-1 * (i + 1))] != ' ':
    #             num.insert(0, equation[(-1 * (i + 1))])
    #             print('In while loop')

    print(resultVector)

    return matrix