N = int(input())
E = int(input())
tree = dict()
for i in range(E):
    start, end = map(int, input().split())
    if start in tree:
        tree[start].append(end)
    else:
        tree[start] = [end]
    if end in tree:
        tree[end].append(start)
    else:
        tree[end] = [start]

def dfs(graph, s):
    if s not in graph:
        return 0
    stack = [s]
    visited = [0]*(N+1)
    while stack:
        node = stack.pop(0)
        if visited[node] == 0:
            visited[node] = 1
            stack.extend(graph[node])
    return sum(visited)-1

print(dfs(tree,1))