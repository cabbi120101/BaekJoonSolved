from collections import deque
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)

result = []
q = deque([(X, 0)])
visited = [0] * (N+1)

while q:
    # print(q)
    sungju, dist = q.popleft()
    if dist == K and visited[sungju] == 0:
        result.append(sungju)
    visited[sungju] = 1

    for i in graph[sungju]:
        if visited[i] == 1:
            continue
        else:
            q.append((i, dist+1))

result = sorted(result)
if result:
    for i in result:
        print(i)
else:
    print('-1')