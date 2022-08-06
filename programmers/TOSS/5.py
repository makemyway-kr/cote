def solution(tasks):
    answer = 0
    levels = {}
    for t in tasks:
        if t not in levels.keys():
            levels[t] = 1
            continue
        levels[t] += 1
    if 1 in levels.values():
        return -1
    for l in levels.keys():
        if levels[l] == 0:
            continue
        if levels[l] == 2 or levels[l] == 3:
            answer += 1
            continue
        if levels[l] % 3 == 0 :
            answer += levels[l]//3
            continue
        elif levels[l] % 3 == 2:
            answer += levels[l]//3 + 1
            continue
        three = levels[l] // 3
        while three >= 0:
            if three == 0 and levels[l] % 2 != 0 :
                answer = -1
                break
            if (levels[l]-(three*3)) % 2 == 0:
                answer += three
                answer += (levels[l]-(three*3))//2
                break
            three -= 1
        if answer == -1:
            break
    return answer