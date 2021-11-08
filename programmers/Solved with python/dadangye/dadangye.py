#프로그래머스 다단계 칫솔판매 문제 https://programmers.co.kr/learn/courses/30/lessons/77486
from math import floor
def solution(enroll, referral, seller, amount):
    indexnum={} #dictionary for each seller's number
    for i in range(len(enroll)):
        indexnum[enroll[i]]=i
    answer = [0 for i in range(len(enroll))]
    for s in range(len(seller)):
        money=amount[s]*100#총 이익금
        answer[indexnum[seller[s]]]+=(money-floor(money*0.1))#10%수수료 제한 금액을 판매한 사람이 가져감
        money=floor(money*0.1)#10%이익금
        curr=referral[indexnum[seller[s]]]#소개해준사람 이름
        while curr!='-':#-가 안나올 때까지 이익금 10%를 떼감.
            curri=indexnum[curr]
            if (money*0.1)>=1:
                answer[curri]+=(money-floor(money*0.1))
                money=floor(money*0.1)
                curr=referral[curri]#소개해준 사람으로 curr을 바꿈.
            else:
                answer[curri]+=money#0.1곱한 것이 1보다 작으면 자기가 다 가짐(이것때문에 틀리다고 나왔었음.)
                break
    return answer