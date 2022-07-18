from math import sqrt,ceil
import sys
N = int(sys.stdin.readline().rstrip())
numbers = [int(x) for x in sys.stdin.readline().rstrip().split()]
answer = 0
for n in numbers:
    if n == 1:
        continue
    elif n == 2 or n == 3:
        answer += 1
        continue
    isPrime = True
    for i in range(2,ceil(sqrt(n))+1):
        if n % i == 0:
            isPrime = False
    if isPrime == True:
        answer += 1
print(answer)
