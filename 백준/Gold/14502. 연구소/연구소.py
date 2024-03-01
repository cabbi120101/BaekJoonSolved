from collections import deque
from itertools import combinations

def bfs(graph):
    # 바이러스 위치 저장
    queue = deque([(i,j) for i in range(N) for j in range(M) if graph[i][j] == 2])
    # 바이러스가 있다면,
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            dr = r + d[i][0]
            dc = c + d[i][1]
            if 0<= dr < N and 0 <= dc < M:
                # 빈 공간이면
                if graph[dr][dc] == 0:
                    # 바이러스 표시
                    graph[dr][dc] = 2
                    # queue에 바이러스 좌표 넣기
                    queue.append((dr,dc))
    global ans
    ans = max(ans, sum(i.count(0) for i in graph))

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
empty_space = [(i, j) for i in range(N) for j in range(M) if arr[i][j] == 0]
ans = 0
for comb in combinations(empty_space, 3):
    # 임시 맵 만들기
    test_map = [i.copy() for i in arr]
    for y, x in comb:
        test_map[y][x] = 1
    bfs(test_map)

print(ans)