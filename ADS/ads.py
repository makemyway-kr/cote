#https://programmers.co.kr/learn/courses/30/lessons/72414#
def solution(play_time, adv_time, logs):
    answer = ''
    play=play_time.split(':')
    adv=adv_time.split(':')
    logs_div=[]
    for i in logs:
        temp=i.split('-')
        for k in temp:
            logs_div.append(k.split(':'))
    curr=[]
    
    return answer
solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])