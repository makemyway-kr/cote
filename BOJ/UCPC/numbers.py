import math
import itertools


def solution():
    answer = 'YES'
    numbers = []
    N = int(input())
    temp = input().split(' ')
    numbers = [int(x) for x in temp]
    can_sort = set()
    combi_nums = itertools.combinations(numbers, 2)
    for c in combi_nums:
        if math.sqrt(c[0]*c[1]) % 1 == 0.0:
            print(math.sqrt(c[0]*c[1]))
            can_sort.add(c)
    for c in can_sort:


solution()
