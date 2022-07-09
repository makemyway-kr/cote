import sys


def split(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        A = split(A, B//2, C)
        return (A * A) % C
    else:
        splitted = split(A, B//2, C)
        return (splitted * splitted * A) % C


def solution():
    A, B, C = map(int, sys.stdin.readline().rstrip().split(' '))
    print(split(A, B, C))


solution()
