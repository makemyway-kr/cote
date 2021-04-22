def nextairport(tickets,depart):
    nominee=[]#갈수있는 공항들 배열
    for i in range(len(tickets)):
        if tickets[i][0]==depart:
            nominee.append([i,tickets[i][1]])
    if len(nominee)>1:
        temp="ZZZ"
        tempin="10005"
        for i in range(len(nominee)):
            if nominee[i][1]<temp:
                temp=nominee[i][1]
                tempin=i
        del tickets[nominee[tempin][0]]
        return nominee[tempin][1]
    elif len(nominee)==1:
        del tickets[nominee[0][0]]
        return nominee[0][1]
def solution(tickets):
    answer = []
    dep=nextairport(tickets,"ICN")
    answer.append("ICN")
    answer.append(dep)
    while len(tickets)!=0: #티켓을 모두 사용할떄까지
        nd=nextairport(tickets,dep)
        answer.append(nd)
        dep=nd
    return answer