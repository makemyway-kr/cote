#프로그래머스 다단계 칫솔판매 문제 https://programmers.co.kr/learn/courses/30/lessons/77486
from math import floor
def solution(enroll, referral, seller, amount):
    indexnum={} #dictionary for each seller's number
    for i in range(len(enroll)):
        indexnum[enroll[i]]=i
    answer = [0 for i in range(len(enroll))]
    for s in range(len(seller)):
        money=amount[s]*100
        answer[indexnum[seller[s]]]+=(money-floor(money*0.1))
        money=floor(money*0.1)
        curr=referral[indexnum[seller[s]]]#소개해준사람 이름
        while True:
            curri=indexnum[curr]
            if floor(money*0.1)>=1 and curr!='-' and referral[curri]!='-':
                answer[curri]+=(money-floor(money*0.1))
                money=floor(money*0.1)
                curr=referral[curri]
            elif referral[curri]=='-':
                
            elif curr=='-':
            else:
                break
    return answer