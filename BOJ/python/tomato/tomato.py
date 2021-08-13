def arrayinput():
    n=int(input())#행의 수
    arrays=[]
    arrays.append(n)
    for r in range(n):
        temp=list(map(int,input().split()))#문자열을 split하고, int가 담긴 list의 형태로 만듦.
        arrays.append(temp)
    return arrays
def solution():
    