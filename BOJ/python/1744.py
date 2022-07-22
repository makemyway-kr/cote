import sys
numbers = []
N = int(sys.stdin.readline().rstrip())

for i in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
numbers.sort(key=lambda x: -x)

answer = 0
last = -1
n = 0
while n < len(numbers)-1:
    if numbers[n] == 1 and numbers[n+1] == 1:
        answer += numbers[n]
        last = n
        n += 1
    elif numbers[n] > 0 and numbers[n+1] == 0:
        answer += numbers[n]
        last = n
        n += 1
    elif numbers[n] * numbers[n+1] < 0:
        answer += numbers[n]
        last = n
        n += 1
    else:
        answer += (numbers[n]*numbers[n+1])
        last = n+1
        n += 2
if last <= len(numbers)-1:
    for i in range(last+1, len(numbers)):
        answer += numbers[i]
print(answer)
