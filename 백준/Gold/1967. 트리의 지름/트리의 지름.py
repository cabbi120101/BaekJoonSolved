import sys
sys.setrecursionlimit(10**6)
n = int(input())
# 그래프 만들기
graph = dict()
for _ in range(n-1):
    start_node, end_node, weight = map(int, input().split())
    graph[start_node] = graph.get(start_node, []) + [(end_node, weight)]
    graph[end_node] = graph.get(end_node, []) + [(start_node, weight)]

def dfs(start, res):
    if start not in graph:
        return 
    for node, w in sorted(graph[start],key=lambda x:x[0]):
        if visited[node]:
            continue
        visited[node] = res + w
        dfs(node, res+w)

# 1부터 시작하기
visited = [0]*(n+1)
visited[1] = 1
dfs(1,0)
visited[1] = 0
# 루트 노드부터 했을 때 가장 가중치가 컸던 node 찾음
# 컸던 노드 부터 탐색해서 가장 가중치가 큰 길 찾음
max_node = visited.index(max(visited))
visited = [0]*(n+1)
visited[max_node] = 1
dfs(max_node,0)
visited[max_node] = 0

print(max(visited))
