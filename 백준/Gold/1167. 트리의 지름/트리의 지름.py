import sys
V = int(sys.stdin.readline())
graph = dict()
for i in range(1,V+1):
    node_num,*info,end_num = list(map(int,sys.stdin.readline().split()))
    for i in range(len(info) // 2):
        if node_num in graph:
            graph[node_num] += [(info[i*2], info[i*2+1])]
        else:
            graph[node_num] = [(info[i * 2], info[i * 2 + 1])]
        if info[i*2] in graph:
            graph[info[i*2]] += [(node_num, info[i*2+1])]
        else:
            graph[info[i * 2]] = [(node_num, info[i * 2 + 1])]

def dfs(start, res):
    if start not in graph:
        return
    for node, w in sorted(graph[start],key=lambda x:x[0]):
        if visited[node]:
            continue
        visited[node] = res + w
        dfs(node, res+w)

# 1부터 시작하기
visited = [0]*(V+1)
visited[1] = 1
dfs(1,0)
visited[1] = 0
# 루트 노드부터 했을 때 가장 가중치가 컸던 node 찾음
# 컸던 노드 부터 탐색해서 가장 가중치가 큰 길 찾음
max_node = visited.index(max(visited))
visited = [0]*(V+1)
visited[max_node] = 1
dfs(max_node,0)
visited[max_node] = 0

print(max(visited))