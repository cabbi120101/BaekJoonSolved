def solution(edges):
    graph = dict()
    for start, end in edges:
        if start in graph:
            graph[start][0] += 1
        else: # out, in
            graph[start] = [1,0]
        if end in graph:
            graph[end][1] += 1
        else:
            graph[end] = [0,1]
    
    ans = [0,0,0,0]
    for node, count in graph.items():
        # 시작 점
        if count[0] >= 2 and count[1]==0:
            ans[0] = node
        # 막대 그래프
        elif count[0] == 0 and count[1] >= 1:
            ans[2] += 1
        # 8자 그래프
        elif count[0] >= 2 and count[1]>=2:
            ans[3] += 1
    ans[1] = graph[ans[0]][0] - ans[2] - ans[3]
    return ans
    
    