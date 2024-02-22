def sort_node(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    L,E,R = [],[],[]
    for i in arr:
        if i < pivot:
            L.append(i)
        elif i == pivot:
            E.append(i)
        else:
            R.append(i)
    return sort_node(L)+E+sort_node(R)

def DFS(graph, start):
    if start not in graph:
        dfs_res.append(start)
    else:
        stack = [start]
        visited = [0]*(N+1)
        while stack:
            node = stack.pop()
            if visited[node] == 0:
                visited[node] = 1
                dfs_res.append(node)
                stack.extend(sort_node(graph[node])[::-1])

def BFS(graph, start):
    if start not in graph:
        bfs_res.append(start)
    else:
        stack = [start]
        visited = [0]*(N+1)
        while stack:
            node = stack.pop(0)
            if visited[node] == 0:
                visited[node] = 1
                bfs_res.append(node)
                stack.extend(sort_node(graph[node]))

N, M, V = map(int, input().split())
graph = dict()
for i in range(M):
    start, end = map(int, input().split())
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]

    if end in graph:
        graph[end].append(start)
    else:
        graph[end] = [start]

dfs_res = []
DFS(graph, V)
print(*dfs_res)

bfs_res = []
BFS(graph,V)
print(*bfs_res)