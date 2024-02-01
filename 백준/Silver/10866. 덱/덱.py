import sys

input = sys.stdin.readline

n = int(input())
deq = []
for _ in range(n):
    request = input().rstrip('\n')
    if 'push_front' in request:
        x = request.split()[1]
        deq.insert(0,int(x))
    elif 'push_back' in request:
        x = request.split()[1]
        deq.append(int(x))
    elif 'pop_front' in request:
        print(deq.pop(0) if deq else -1)
    elif 'pop_back' in request:
        print(deq.pop() if deq else -1)
    elif request=='size':
        print(len(deq))
    elif request=='empty':
        print(1 if len(deq)==0 else 0)
    elif request=='front':
        print(deq[0] if deq else -1)
    elif request=='back':
        print(deq[-1] if deq else -1)