def solution(info, query):
    answer = []
    table={"cpp":[],"java":[],"python":[],"backend":[],"frontend":[],"junior":[],"senior":[],"chicken":[],"pizza":[]}
    table_score={}
    for c in range(len(info)):
        temp_info=info[c].split(" ")
        for t in temp_info:
            if t in table:
                table[t].append(c)
            else:
                table_score[c]=int(t)
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
                else:
                    for each in candidates:
                        if table_score.get(each)<int(cond):
                            toeliminate.append(each)
            for each in toeliminate:
                candidates.remove(each)
        answer.append(len(candidates))
    return answer