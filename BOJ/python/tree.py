import sys
tree = {}


def preorder(curr):
    global tree
    if curr != '.':
        print(curr, end='')
        preorder(tree[curr][0])
        preorder(tree[curr][1])


def midorder(curr):
    global tree
    if curr != '.':
        midorder(tree[curr][0])
        print(curr, end='')
        midorder(tree[curr][1])


def lastorder(curr):
    global tree
    if curr != '.':
        lastorder(tree[curr][0])
        lastorder(tree[curr][1])
        print(curr, end='')


def solution():
    N = int(sys.stdin.readline().rstrip())
    global tree
    root = ''
    for i in range(N):
        temp = sys.stdin.readline().rstrip().split(' ')
        tree[temp[0]] = [temp[1], temp[2]]
        if i == 0:
            root = temp[0]
    preorder(root)
    print()
    midorder(root)
    print()
    lastorder(root)
    print()


solution()
