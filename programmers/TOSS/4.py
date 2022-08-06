def solution(invitationPairs):
    answer = []
    connectionList = {}
    scores = []
    for i in invitationPairs:
        if i[0] not in connectionList.keys():
            connectionList[i[0]] = [i[1]]
            connectionList[i[1]] = []
        else:
            connectionList[i[0]].append(i[1])
            connectionList[i[1]] = []
    for u in connectionList.keys():
        score = 0
        score += len(connectionList[u]) * 10
        for c in connectionList[u]:
            score += len(connectionList[c])*3
            for c2 in connectionList[c]:
                score += len(connectionList[c2])
        scores.append([u,score])
    scores.sort(key = lambda x : -x[1])
    return [x[0] for x in scores[0:3] if x[1] != 0]