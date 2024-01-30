import sys
from collections import deque
N = int(sys.stdin.readline())
Q = deque([])
for _ in range(N):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == 'push':
        Q.append(order[1])
    elif order[0] == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(Q))
    elif order[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)