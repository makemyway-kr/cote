times=[]
def proc_log(line):
    global times
    line=line.split(' ')
    for i in range(len(line[2])):
        if line[2][i]=='s':
            break
    protime=line[2][:i]
    endtime=line[1]
    endtime=endtime.split(':')
    endtime[2]=endtime[2].split('.')
    endtimeinsec=float((60*60*int(endtime[0]))+(60*int(endtime[1]))+int(endtime[2][0])+0.001*int(endtime[2][1]))#change time into second
    starttimeinsec=endtimeinsec-float(protime)+0.001
    times.append([starttimeinsec,endtimeinsec])
def solution(lines):
    if len(lines)==1:
        return 1
    else:
        global times
        for i in lines:#split input and calculate starting time of each log
            proc_log(i)
        times.sort(key=lambda times:times[0])#sort by starting time
        currtime=times[0][0]
        count=0
        interval=0
        if times[len(times)-1][1]-times[0][0]<=60*60*12:#첫 작업~마지막 작업 시간이 12시간을 안넘으면
            interval=0.001
        else:
            interval=0.05

        while currtime<=times[len(times)-1][1]:#until the last process finishes
            temp=0
            for i in times:
                if (i[0]>=currtime and i[0]<=currtime+1) or (i[1]>=currtime and i[1]<=currtime+1):
                    temp+=1
                elif(i[0]>currtime):# 오름차순으로 정렬되어있음으로 시작 시간이 현재시간보다 클 경우 더이상 비교할 필요가 없음.
                    break
            if temp>count:
                count=temp 
            currtime+=interval
    return count