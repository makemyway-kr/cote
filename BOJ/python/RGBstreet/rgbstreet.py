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
    for house in range(1,inputs[0]):
        inputs[house+1][0]+=min(inputs[house][1],inputs[house][2])
        inputs[house+1][1]+=min(inputs[house][0],inputs[house][2])
        inputs[house+1][2]+=min(inputs[house][0],inputs[house][1])
    print(min(inputs[inputs[0]]))
solution()