from collections import deque
N,K = map(int, input().split())
A = deque(map(int,input().split()))
line = deque([False]*N)
ans = 0

while True:
    ans += 1
    A.rotate(1)
    line.rotate(1)

    line[N-1] = False

    for i in range(N-2, -1, -1):
        if line[i] and not line[i+1] and A[i+1] >0:
            line[i],line[i+1] = False, True
            A[i+1] -= 1

    line[N-1] = False

    if A[0] > 0:
        line[0] = True
        A[0] -= 1
    if A.count(0) >= K:
        break

print(ans)