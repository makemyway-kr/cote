import sys
positive = []
zeros = []
negative = []
ones = []
N = int(sys.stdin.readline().rstrip())

for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    if temp > 1:
        positive.append(temp)
    elif temp == 1:
        ones.append(temp)
    elif temp == 0:
        zeros.append(temp)
    else:
        negative.append(temp)
positive.sort(key=lambda x: -x)
negative.sort()

answer = 0
while len(positive) > 1:
    t1 = positive.pop(0)
    t2 = positive.pop(0)
    answer += t1*t2
if len(positive) > 0:
    answer += positive.pop()
while(len(negative)) > 1:
    answer += (negative.pop(0)*negative.pop(0))
if len(zeros) > 0 and len(negative) > 0:
    negative.pop(0)
elif len(zeros) == 0 and len(negative) > 0:
    answer += negative.pop(0)
answer += len(ones)
print(answer)
