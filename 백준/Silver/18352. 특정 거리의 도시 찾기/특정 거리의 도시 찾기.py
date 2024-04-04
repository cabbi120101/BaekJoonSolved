import sys
import heapq
def f(graph,start):
    distances[start] = 0
    q = []
    heapq.heappush(q,[distances[start],start])
    while q:
        cost,node = heapq.heappop(q)
        if distances[node] < cost:
            continue
        for next_node, next_cost in graph[node].items():
            dist = cost + next_cost
            if dist < distances[next_node]:
                distances[next_node] = dist
                heapq.heappush(q,[dist,next_node])


n,m,k,x = map(int,sys.stdin.readline().split())
graph = {i:{} for i in range(1,n+1)}
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].update({b:1})
distances = {i:float("inf") for i in range(1,n+1)}
f(graph,x)
flag= True
for x,y in distances.items():
    if y == k:
        print(x)
        flag = False
if flag:
    print(-1)