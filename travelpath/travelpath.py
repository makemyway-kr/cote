import heapq
used_ticket=[]
def nextairport(tickets,depart):#dfs
    nominee=[]#갈수있는 공항들 배열
    for i in range(len(tickets)):
        if tickets[i][0]==depart:
            heapq.heappush(nominee,(tickets[i][1],i))
    
def solution(tickets):
    answer = []
    dep=nextairport(tickets,"ICN")
    answer.append("ICN")
    answer.append(dep)
    count=2
    while count=len(tickets)+1: #티켓을 모두 사용할떄까지
        nd=nextairport(tickets,dep)
        answer.append(nd)
        dep=nd
        count+=1
    return answer