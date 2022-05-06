from itertools import combinations
from operator import indexOf
from itertools import combinations
def solution(orders,course):
    answer = []
    orders.sort ( key = lambda x : len(x))
    for c in course:
        if c > len(orders[-1]):
            course.pop(indexOf(course,c))
    for c in course:
        candidates = {}
        for o in orders:
            if c <= len(o):
                temp = list(combinations(o,c))
                for t in temp:
                    st = "".join(sorted(t))
                    if st not in candidates.keys():
                        candidates[st] = 1
                    else:
                        candidates[st] += 1
        max_ordered = max(candidates.values())
        if max_ordered >= 2:
            for k in candidates.keys():
                if candidates[k] == max_ordered:
                    answer.append("".join(sorted(k)))
    return list(sorted(answer))