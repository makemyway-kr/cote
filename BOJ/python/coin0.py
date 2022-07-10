import sys
coins = []
N, K = map(int, sys.stdin.readline().rstrip().split(' '))
for i in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))
coins.sort(key=lambda x: -x)
curr = 0
answer = 0
for c in coins:
    if c <= K-curr:
        temp = (K-curr)//c
        answer += temp
        curr += temp*c
print(answer)
