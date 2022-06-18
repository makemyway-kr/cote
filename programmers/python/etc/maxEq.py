#수식최대화
from itertools import permutations
import copy
def solution(expression):
    answer = 0
    operators = ['*','-','+']
    shown_operators = set()
    operator_position = []
    count = 0
    expression = list(expression)
    for e in range(len(expression)):
        if expression[e] in operators:
            shown_operators.add(expression[e])
            operator_position.append([expression[e],count])#(연산자,위치)
            expression[e] = 'X'
            count += 1
    expression = ''.join(expression)
    expression = expression.split('X')
    expression = [int(i) for i in expression]
    for per in list(permutations(list(shown_operators))):
        temp_operator_position = copy.deepcopy(operator_position)
        temp_expression = copy.deepcopy(expression)
        for o in per:
            for each_oper in temp_operator_position:
                if each_oper[0] == o:
                    temp_position = each_oper[1]
                    if o == '*':
                        temp_expression[temp_position] = temp_expression[temp_position] * temp_expression[temp_position+1]
                    elif o == '+':   
                        temp_expression[temp_position] = temp_expression[temp_position] + temp_expression[temp_position+1]
                    elif o == '-':
                        temp_expression[temp_position] = temp_expression[temp_position] - temp_expression[temp_position+1]
                    temp_expression.pop(temp_position+1)
                    for i in temp_operator_position:
                        if i[1] > temp_position:
                            i[1] -= 1
        if temp_expression[0] < 0:
            temp_expression[0] = -(temp_expression[0])
        if answer < temp_expression[0]:
            answer = temp_expression[0]
    return answer