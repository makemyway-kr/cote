import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

ways = [0 for x in range(0, K+1)]
ways[0] = 1
coins = []
for i in range(N):
    c = int(sys.stdin.readline().rstrip())
    coins.append(c)

for c in coins:
    for w in range(c, K+1):
        if ways[w-c] != 0:
            ways[w] += ways[w-c]
print(ways[K])
