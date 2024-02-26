def chk(y,x):
    if 0<= y < M and 0<= x < N:
        if arr[y][x] == 1:
            arr[y][x] = 0
            chk(y+1, x)
            chk(y-1, x)
            chk(y, x+1)
            chk(y, x-1)
            return True
        else:
            return False
    else:
        return False
import sys
sys.setrecursionlimit(10**9)
T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    ans = 0
    for i in range(M):
        for j in range(N):
            if chk(i,j) == True:
                ans += 1
    print(ans)