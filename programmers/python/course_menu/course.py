from itertools import combinations
def solution(orders,course):
    answer = []
    orders.sort ( key = lambda x : len(x))

    return orders