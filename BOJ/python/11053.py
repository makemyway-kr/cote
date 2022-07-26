import sys

N = int(sys.stdin.readline().rstrip())

numbers = [int(x) for x in sys.stdin.readline().rstrip().split()]
maxlengths = [0 for x in range(N)]
maxlengths[0] = 1

for n in range(1, N):
    temp = 0
    for c in range(0, n):
        if numbers[c] < numbers[n] and maxlengths[c] > temp:
            temp = maxlengths[c]
    maxlengths[n] = temp + 1

print(max(maxlengths))
