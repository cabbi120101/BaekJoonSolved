def DFS(graph, start):
    stack = [start]
    visited = [0]*(N+1)
    while stack:
        node = stack.pop()
        for i in graph[node]:
            if visited[i] == 0:
                res[i] = node
                visited[i] = 1
                stack.append(i)

N = int(input())
graph = dict()
for _ in range(N-1):
    start, end = map(int, input().split())
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]

    if end in graph:
        graph[end].append(start)
    else:
        graph[end] = [start]

res = [0]*(N+1)
DFS(graph, 1)
for i in range(2, N+1):
    print(res[i])