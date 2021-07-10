def solution(info, query):
    answer = []
    table={"cpp":[],"java":[],"python":[],"backend":[],"frontend":[],"junior":[],"senior":[],"chicken":[],"pizza":[]}
    table_score=[]
    for c in range(len(info)):
        temp_info=info[c].split(" ")
        for t in temp_info:
            if t in table:
                table[t].append(c)
            else:
                table_score.append([c,t])
    table_score.sort(key= lambda table_score:table_score[1])
    for k in query:
        temp=k.split(" ")
        candidates=[]
        for cd in range(len(info)):
            candidates.append(cd)
        for cond in temp:
            toeliminate=[]
            if cond!="and" and cond!='-':
                if cond in table:
                    for each in candidates:
                        if each not in table[cond]:
                            toeliminate.append(each)
                else:#score
                    
                    for each in candidates:
                        if table_score.get(each)<int(cond):
                            toeliminate.append(each)
            for each in toeliminate:
                candidates.remove(each)
        answer.append(len(candidates))
    return answer
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])