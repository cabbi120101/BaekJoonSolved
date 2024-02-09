import sys
T = int(input())
stack = []
for _ in range(T):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)