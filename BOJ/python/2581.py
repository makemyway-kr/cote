import sys
import math
M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
primes = []
for i in range(M, N+1):
    is_prime = True
    if i == 1:
        continue
    elif i == 2:
        primes.append(i)
        continue
    for d in range(2, math.floor(math.sqrt(i))+2):
        if i % d == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(i)
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])
