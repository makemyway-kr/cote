import math

def solution(alp, cop, problems):
    answer = 0
    can = [p for p in problems if p[0] <= alp and p[1] <= cop]
    cant = [ p for p in problems if p not in can]
    cant.sort(key = lambda x : (x[0] - alp)+ (x[1] - cop) )
    can.sort(key = lambda x : (x[2]/x[4])+(x[3]/x[4]))
    curralp = alp
    currcop = cop
    while len(cant) != 0 :
        to_solve = cant.pop(0)
        if curralp > to_solve[0] and currcop > to_solve[1]:
            continue
        elif len(can) == 0:
            studyhour = (to_solve[0] - curralp) + (to_solve[1] - currcop)
            answer += studyhour
            curralp = to_solve[0]
            currcop = to_solve[1]
        else:
            candidate = 301
            for s in can:
                tempanswer = answer
                to_alp = to_solve[0] - curralp
                to_cop = to_solve[1] - currcop
                solvAlp = to_alp / s[2]
                solvCop = to_cop / s[3]
                temp_cop = currcop
                temp_alp = curralp
                if solvAlp <= 0 :
                    tempanswer += int(solvCop) * to_solve[4]
                elif solvCop <=0 :
                    tempanswer += int(solvAlp) * to_solve[4]
                else:
                    tempanswer += min(int(solvCop),int(solvAlp)) * to_solve[4]
                if temp
        can.append(to_solve)
        can.sort(key = lambda x : (x[2]/x[4])+(x[3]/x[4]))
    return answer