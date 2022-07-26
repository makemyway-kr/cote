import sys

candidates = []


def recursive(level, n):
    if n == 1:
        candidates.append(level)
        return
    if n % 2 == 0:
        recursive(level+1, n//2)
    if n % 3 == 0:
        recursive(level+1, n//3)
    if n > 1:
        recursive(level+1, n-1)


N = int(sys.stdin.readline().rstrip())
recursive(0, N)
print(min(candidates))
