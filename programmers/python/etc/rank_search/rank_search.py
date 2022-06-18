#lv2 순위검색
def solution(info, query):
    answer = []
    language = {}
    job = {}
    career = {}
    food = {}
    scores = {}
    for i in range(len(info)):
        temp = info[i].split(' ')
        if temp[0] not in language.keys():
            language[temp[0]] = [i]
        else:
            language[temp[0]].append(i)
        if temp[1] not in job.keys():
            job[temp[1]] = [i]
        else:
            job[temp[1]].append(i)
        if temp[2] not in career.keys():
            career[temp[2]] = [i]
        else:
            career[temp[2]].append(i)
        if temp[3] not in food.keys():
            food[temp[3]] = [i]
        else:
            food[temp[3]].append(i)
        scores[i] = int(temp[4])
    for q in query:
        temp = q.split(' ')
        candidate = set([i for i in range(len(info)) if scores[i] >= temp[7]])
        for t in range(len(temp)):
            if temp[t] != '-' and temp[t]!= 'and':
                if t == 0:
                    candidate = candidate & set(language[temp[t]])
                elif t == 2:
                    candidate = candidate & set(job[temp[t]])
                elif t == 4:
                    candidate = candidate & set(career[temp[t]])
                elif t == 6:
                    candidate = candidate & set(food[temp[t]])
        answer.append(len(candidate))
    return answer