def solution(info, query):
    answer = []
    table_language={"cpp":[],"java":[],"python":[]}
    table_part={"backend":[],"frontend":[]}
    table_career={"junior":[],"senior":[]}
    table_food={"chicken":[],"pizza":[]}
    table_score={}
    for c in range(len(info)):
        temp_info=info[c].split(" ")
        for t in temp_info:
            if t=="java" or t=="cpp" or t=="python":
                table_language[t].append(c)
            elif t=="backend" or t=="frontend":
                table_part[t].append(c)
            elif t=="junior" or t=="senior":
                table_career[t].append(c)
            elif t=="chicken" or t=="pizza":
                table_food[t].append(c)
            else:
                table_score[c]=int(t)
    for k in query:
        temp=k.split(" ")
        candidates=[]
        for cd in range(len(info)):
            candidates.append(cd)
        for cond in temp:
            if cond!="and" and cond!='-':
                if cond=="java" or cond=="cpp" or cond=="python":
                    for each in candidates:
                        if each not in table_language[cond]:
                            candidates.remove(each)
                elif cond=="backend" or cond=="frontend":
                    for each in candidates:
                        if each not in table_part[cond]:
                            candidates.remove(each)
                elif cond=="junior" or cond=="senior":
                    for each in candidates:
                        if each not in table_career[cond]:
                            candidates.remove(each)
                elif cond=="chicken" or cond=="pizza":
                    for each in candidates:
                        if each not in table_food[cond]:
                            candidates.remove(each)
                else:
                    for each in candidates:
                        if table_score.get(each)<int(cond):
                            candidates.remove(each)
        answer.append(len(candidates))
    return answer
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])