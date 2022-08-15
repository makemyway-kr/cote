import sys

x = []
y = []
for i in range(3):
    t1, t2 = map(int, sys.stdin.readline().rstrip().split())
    x.append(t1)
    y.append(t2)

a1 = y[1]-y[0]
a2 = x[1]-x[0]
a = 0
b = 0
if a2 != 0:
    a = a1/a2
    b = y[0]-(x[0]*(a))
    c = (x[2]*(a)) + b
    if c == y[2]:
        print(0)
    elif c < y[2]:  # p1,p2를 이은 직선보다 위에 p3점이 위치하면 반시계
        print(1)
    else:  # p1,p2를 이은 직선보다 아래에 p3점이 위치하면 시계방향
        print(-1)
else:  # x=c 형태의 직선인 경우
    if x[2] == x[1]:
        print(0)
    elif x[2] < x[1]:
        print(1)
    else:
        print(-1)
