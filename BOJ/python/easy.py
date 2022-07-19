# 쉬운문제용 연습장
import sys
N = int(sys.stdin.readline().rstrip())
temp = []
for i in range(N):
    temp.append(int(sys.stdin.readline().rstrip()))
temp.sort(key=lambda x: -x)
for i in range(N):
    print(temp[i])
