from operator import indexOf
def solution(n, costs):
    answer = 0
    visitied = set()
    groups = []
    costs.sort(key = lambda x : x[2])
    while len(visitied) != n or len(groups) != 1:
        if costs[0][0] not in visitied and costs[0][1] not in visitied:
            visitied.add(costs[0][0])
            visitied.add(costs[0][1])
            answer += costs[0][2]
            groups.append([costs[0][0],costs[0][1]])
            costs.pop(0)
        elif costs[0][0] in visitied and costs[0][1] not in visitied:
            visitied.add(costs[0][1])
            answer += costs[0][2]
            temp = 0
            for g in groups:
                if costs[0][0] in g:
                    temp = indexOf(groups,g)
                    break
            groups[temp].append(costs[0][1])
        elif costs[0][0] not in visitied and costs[0][1] in visitied:
            visitied.add(costs[0][0])
            answer += costs[0][2]
            temp = 0
            for g in groups:
                if costs[0][1] in g:
                    temp = indexOf(groups,g)
                    break
            groups[temp].append(costs[0][0])
        elif costs[0][0] in visitied and costs[0][1] in visitied:
            g1 = None
            g2 = None
            for g in groups:
                if costs[0][0] in g:
                    g1 = indexOf(groups,g)
                if costs[0][1] in g:
                    g2 = indexOf(groups,g)
                if g1 is not None and g2 is not None:
                    break
            if g1 != g2 and (g1 is not None and g2 is not None):
                answer += costs[0][2]
                if g1 == 0:
                    for g in groups[g2]:
                        groups[0].append(g)
                    groups.pop(g2)
                elif g2 == 0:
                    for g in groups[g1]:
                        groups[0].append(g)
                    groups.pop(g1)
                else:
                    for g in groups[g2]:
                        groups[g1].append(g)
                    groups.pop(g2)
            costs.pop(0)
            
    return answer
print(solution(4,[[0,1,1],[2,3,2],[0,3,3]]))