import sys

x = []
y = []
for i in range(3):
    t1, t2 = map(int, sys.stdin.readline().rstrip().split())
    x.append(t1)
    y.append(t2)

ccw = (x[0]*y[1]+x[1]*y[2]+x[2]*y[0])-(x[1]*y[0]+x[2]*y[1]+x[0]*y[2])
if ccw == 0:
    print(0)
elif ccw > 0:
    print(1)
elif ccw < 0:
    print(-1)
