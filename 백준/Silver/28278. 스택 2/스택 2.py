import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    item = list(map(int, sys.stdin.readline().split()))
    if item[0] == 1:
        stack.append(item[1])
    elif item[0] == 2:
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print(-1)
    elif item[0] == 3:
        print(len(stack))
    elif item[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)