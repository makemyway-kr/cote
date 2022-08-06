def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    answer = []
    steps = {}
    for n in range(len(names_one)):
        if names_one[n] not in steps.keys():
            steps[names_one[n]] = [steps_one[n],0,0]
        else:
            if len(steps[names_one[n]][0]) != 0:
                if steps_one[n] > steps[names_one[n]][0]:
                    steps[names_one[n]][0] = steps_one[n]
            else:
                steps[names_one[n]][0] = steps_one[n]
    for n in range(len(names_two)):
        if names_two[n] not in steps.keys():
            steps[names_two[n]] = [0,[steps_two[n]],[]]
        else:
            if len(steps[names_two[n]][1]) != 0:
                if steps_two[n] > steps[names_two[n]][1]:
                    steps[names_two[n]][1] = steps_two[n]
            else:
                steps[names_two[n]][1] = steps_two[n]
    for n in range(len(names_three)):
        if names_three[n] not in steps.keys():
            steps[names_three[n]] = [[],[],[steps_three[n]]]
        else:
            if len(steps[names_three[n]][2]) != 0:
                if steps_three[n] > steps[names_three[n]][2]:
                    steps[names_three[n]][2] = steps_three[n]
            else:
                steps[names_three[n]][2] = steps_three[n]
    step_sum = [sum(steps[x][0],steps[x][1],steps[x][2]) for x in steps.keys()]
    print(step_sum)
    return answer