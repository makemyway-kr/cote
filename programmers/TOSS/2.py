def solution(levels):
    answer = -1
    if len(levels) < 4:
        return answer
    cut = len(levels)//4
    levels.sort()
    answer = levels[-cut]
    return answer