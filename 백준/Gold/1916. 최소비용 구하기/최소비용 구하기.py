import heapq
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
# 그래프 만들기
graph = dict()
for _ in range(M):
    start_node, end_node, weight = map(int, sys.stdin.readline().split())
    if start_node in graph:
        graph[start_node] += [(end_node,weight)]
    else:
        graph[start_node] = [(end_node,weight)]
start, end = map(int, sys.stdin.readline().split())
# 다익스트라
def dijkstra(start):
    # 초기 값은 최대 값으로 설정
    distances = [1e9]*(N+1)
    # 시작하는 노드는 0
    distances[start] = 0
    queue = []
    # 시작 노드부터 탐색 시작
    heapq.heappush(queue, [distances[start], start])
    while queue:
        # 탐색할 거리, 노드
        dist, node = heapq.heappop(queue)

        # 기존 최단거리보다 멀다면 무시
        if distances[node] < dist:
            continue
        if node not in graph:
            continue
        # 노드와 연결된 인접노드 탐색
        for next_node, next_dist in graph[node]:
            # 인접노드까지의 거리
            distance = dist + next_dist
            # 기존 거리 보다 짧으면 갱신
            if distance < distances[next_node]:
                distances[next_node] = distance
                # 다음 인접 거리를 계산 하기 위해 큐에 삽입
                heapq.heappush(queue, [distance, next_node])
    return distances
print(dijkstra(start)[end])