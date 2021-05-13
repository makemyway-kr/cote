win=[];
lose=[];
def winorlose(n,results):
    global win;#이긴 상대 저장
    global lose;#진 상대 저장
    win=[[]for players in range(n+1)]
    lose=[[]for player in range(n+1) ]
    for i in results:
        win[i[0]].append(i[1])
        lose[i[1]].append(i[0])
    for i in range(1,n+1):
        if len(lose[i])>0: # 나를 이긴 상대가 진 상대면 무조건 나도 짐
            for k in lose[i]:
                if len(lose[k])>0:
                    for j in lose[k]:
                        if j not in lose[i]:
                            lose[i].append(j)
    for i in range(1,n+1):
        if len(win[i])>0:
            for k in win[i]:#내가 이긴 상대가 이긴 상대면 무조건 나도 이김.
                if len(win[k])>0:
                    for j in win[k]:
                        if j not in win[i]:
                            win[i].append(j)
def solution(n, results):
    global win;
    global lose;
    winorlose(n,results)
    answer=0
    for i in range(n+1):
        if len(win[i])+len(lose[i])==n-1:
            answer+=1
    return answer
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))