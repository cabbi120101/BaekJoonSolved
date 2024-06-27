N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

def bfs_exterior():
    queue = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return visited

def mark_melting_cheese(visited):
    melting = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                count = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if visited[ni][nj]:
                        count += 1
                if count >= 2:
                    melting.append((i, j))
    return melting

def melt_cheese(melting):
    for i, j in melting:
        board[i][j] = 0

def all_cheese_melted():
    for row in board:
        if 1 in row:
            return False
    return True

time = 0

while not all_cheese_melted():
    visited = bfs_exterior()
    melting_cheese = mark_melting_cheese(visited)
    melt_cheese(melting_cheese)
    time += 1

print(time)