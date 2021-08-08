used_ticket=[]
def next(tickets,curr,used):
    count=0
    for i in range(len(tickets)):
        if tickets[i][0]==curr and i not in used:
            count+=1
            used.append(i)
            if next(tickets,tickets[i][1],used)==-1 and len(used_ticket)<len(tickets)-1:#티켓을 다 쓰지 못했는데 다음 공항이 안나오는 경우 back
                used.remove(i)#티켓을 사용하지 않은걸로!
                count-=1
    if count==0:
        return -1
def solution(tickets):
    tickets.sort(key=lambda tickets :tickets[1])#도착지 이름 알파벳 순서대로 정렬
    print(tickets)
    global used_ticket
    answer=["ICN"]
    next(tickets,"ICN",used_ticket)
    for i in used_ticket:
        answer.append(tickets[i][1])
    return answer
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))