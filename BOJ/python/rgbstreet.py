#https://www.acmicpc.net/problem/1149
def arrayinput():
    n=int(input())
    costs=[]
    costs.append(n)
    for r in range(n):
        temp=list(map(int,input().split()))
        costs.append(temp)
    return costs
def solution():
    inputs=arrayinput()
    answer=0
    back_color=-1
    for curr in range(inputs[0]):
        min=1001
        for color in range(3):
            if inputs[curr+1][color]<min and color!=back_color:
                back_color=color
                min=inputs[curr+1][color]
        answer+=min
    print("answer",answer)
    return answer
solution()