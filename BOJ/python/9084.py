import sys
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    cSize = int(sys.stdin.readline().rstrip())
    coins = [int(x) for x in sys.stdin.readline().rstrip().split()]
    K = int(sys.stdin.readline().rstrip())
    ways = [0 for i in range(K+1)]
    ways[0] = 1
    for c in coins:
        for k in range(1,K+1):
            if k-c >= 0:
                if ways[k-c] != 0:
                    ways[k] += ways[k-c]
    print(ways[-1])

