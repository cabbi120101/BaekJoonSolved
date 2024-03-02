from collections import deque
from itertools import combinations

def bfs(graph):
    # 바이러스 위치 저장
    queue = deque([(i,j) for i in range(N) for j in range(N) if graph[i][j] == 2])
    # 바이러스가 있다면,
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            dr = r + d[i][0]
            dc = c + d[i][1]
            if 0<= dr < N and 0 <= dc < N:
                # 빈 공간이면
                if graph[dr][dc] == 0:
                    # 바이러스 표시
                    graph[dr][dc] = graph[r][c] + 1
                    # queue에 바이러스 좌표 넣기
                    queue.append((dr,dc))
    if sum(i.count(0) for i in graph) == 0:
        temp = 0
        for i in graph:
            temp = max(temp, max(i))
        global ans
        ans = min(ans, temp-2)

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v_space = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 2]
ans = 1e9
for comb in combinations(v_space, len(v_space)-M):
    # 임시 맵 만들기
    test_map = [i.copy() for i in arr]
    for y, x in comb:
        test_map[y][x] = 0

    bfs(test_map)

print(ans if ans != 1e9 else -1)