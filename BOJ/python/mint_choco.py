def getInput():
    n = int(input())
    equation = input()
    return n, equation
def solution():
    n, equation = getInput()
    equation = equation.split(' ')
    temp = float(equation[0])
    numbers = [float(equation[i]) for i in range(len(equation)) if i % 2 == 0]
    sign = [equation[i] for i in range(len(equation)) if i%2 == 1]
    for s in range(len(sign)):
        if sign[s] == '*':
            temp *= numbers[s+1]
        else:
            temp /= numbers[s+1]
    if temp % 1 == 0:
        print('mint chocolate')
        return ('mint chocolate')
    else:
        print('toothpaste')
        return 'toothpaste'

solution()