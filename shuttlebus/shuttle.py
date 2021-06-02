#https://programmers.co.kr/learn/courses/30/lessons/17678
def solution(n, t, m, timetable):
    a_hour=0
    a_minute=0
    answer = ""
    times=[]
    for i in timetable:
        temp=i.split(':')
        times.append([int(temp[0]),int(temp[1])])
    times.sort()
    bus_passengers=[]
    hour=9
    minute=0
    bus=0
    while bus<n:
        temp=[]
        for k in times:
            if (k[0]<hour or (k[0]==hour and k[1]<=minute)) and len(temp)<m:
                temp.append([k[0],k[1]])
            else:
                break
        bus_passengers.append(temp)
        for k in temp:
            times.remove(k)
        if bus==n-1:
            a_hour=hour
            a_minute=minute
        bus+=1
        minute+=t
        if minute>=60:
            hour+=1
            minute-=60
    if len(bus_passengers[n-1])==m:#마지막 버스를 조사했을때 꽉 차있으면
        if(bus_passengers[n-1][m-1][1]==0):
            a_minute=59
            a_hour=bus_passengers[n-1][m-1][0]-1
        else:
            a_hour=bus_passengers[n-1][m-1][0]
            a_minute=bus_passengers[n-1][m-1][1]-1
    if((a_hour/10)<1):
        answer+=("0"+str(a_hour))
    else:
        answer+=str(a_hour)
    answer+=":"
    if((a_minute/10)<1):
        answer+=("0"+str(a_minute))
    else:
        answer+=str(a_minute)
    return answer
ans=solution(1,1,5,	["08:00", "08:01", "08:02", "08:03"])
print(ans)