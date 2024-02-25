N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
d = [(0,1),(1,0),(-1,0),(0,-1)]
def BFS(y,x):
    stack = [(y,x)]
    while stack:
        y, x = stack.pop(0)
        for i in range(4):
            dy = y + d[i][0]
            dx = x + d[i][1]
            if 0 <= dy < N and 0 <= dx < M and arr[dy][dx] == 1:
                stack.append((dy,dx))
                arr[dy][dx] = arr[y][x] + 1
    return arr[N-1][M-1]

print(BFS(0,0))