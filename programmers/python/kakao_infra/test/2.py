from operator import indexOf
def solution(queue1, queue2):
    answer = 0
    to_match = int((sum(queue1) + sum(queue2)) / 2)
    if (sum(queue1)+sum(queue2))%2 != 0:
        answer = -1
    elif sum(queue1) == sum(queue2):
        answer = 0
    elif max(queue1) > to_match or max(queue2) > to_match :
        answer = -1
    else:
        if to_match in queue1 :
            if queue1[-1] != to_match:
                answer = len(queue2) + (indexOf(queue1,to_match) * 2) + 1
            else:
                answer = len(queue1) - 1
        elif to_match in queue2 :
            if queue2[-1] != to_match:
                answer = len(queue2) + (indexOf(queue2,to_match) * 2) + 1
            else:
                answer = len(queue2) - 1
        else:
            while sum(queue1) != sum(queue2) and answer < 2*len(queue1):
                if sum(queue1) > sum(queue2):
                    while sum(queue1) > sum(queue2) and answer < 2*len(queue1):
                        queue2.append(queue1.pop(0))
                        answer += 1
                else:
                    while sum(queue1) < sum(queue2) and answer < 2*len(queue1):
                        queue1.append(queue2.pop(0))
                        answer +=1
            if answer >= 2*len(queue1):
                return -1
    return answer