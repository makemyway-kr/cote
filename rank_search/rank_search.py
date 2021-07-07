def solution(info, query):
    answer = []
    table_language={}
    table_part={}
    table_career={}
    table_food={}
    table_score={}
    for k in query:
        temp=k.split(" ")
        candidates=[]
        for cond in temp:
            if cond!="and" and cond!='-':
                print(cond)
    return answer
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])