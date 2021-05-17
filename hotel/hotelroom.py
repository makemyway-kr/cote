import sys
sys.setrecursionlimit(1000000)
answer=[]
roomnumber=0
def check(wanted):
    global answer
    if wanted not in answer and wanted<=roomnumber:
            answer.append(wanted)
    else:
        check(wanted+1)
def solution(k, room_number):
    global answer
    global roomnumber
    roomnumber=k
    for i in room_number:
        check(i)
    return answer