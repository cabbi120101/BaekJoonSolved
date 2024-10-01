from collections import deque
n = int(input())
m = int(input())

graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

chin = graph[1] + [j for i in graph[1] for j in graph[i] if j != 1]
chin = list(set(chin))
print(len(chin))