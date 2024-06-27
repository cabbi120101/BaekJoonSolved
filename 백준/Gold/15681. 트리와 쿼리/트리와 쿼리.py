import sys

sys.setrecursionlimit(200000)

N, R, Q = map(int, sys.stdin.readline().split())
node_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    U,V = map(int, sys.stdin.readline().split())
    node_list[U].append(V)
    node_list[V].append(U)

def make_tree(current, parent):
    for node in node_list[current]:
        if node != parent:
            child[current].append(node)
            make_tree(node, current)


# 자식 리스트를 저장할 딕셔너리 초기화
child = {i: [] for i in range(1, N + 1)}

# 트리 구조 생성
make_tree(R, -1)

def count_subtree(current):
    subtree_size[current] = 1
    for node in child[current]:
        count_subtree(node)
        subtree_size[current] += subtree_size[node]

# 서브트리 크기를 저장할 리스트 초기화
subtree_size = [0] * (N + 1)

# 서브트리 크기 계산
count_subtree(R)

for _ in range(Q):
    U = int(sys.stdin.readline())
    print(subtree_size[U])