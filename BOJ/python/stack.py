import sys


def solution():
    N = int(sys.stdin.readline().rstrip())
    stack = []
    for i in range(N):
        command = sys.stdin.readline().rstrip()
        if command == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif command == 'size':
            print(len(stack))
        elif command == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        else:
            stack.append(command.split(' ')[1])


solution()
