import sys
from collections import deque
T = int(input())
q = deque()
for _ in range(T):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        q.append(a[1])
    elif a[0] == 'pop':
        print(q.popleft() if q else -1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        print(0 if q else 1)
    elif a[0] == 'front':
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)