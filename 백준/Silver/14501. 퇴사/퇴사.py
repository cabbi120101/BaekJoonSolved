import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
consult_list = []
for i in range(n):
    t,p = map(int,input().split())
    consult_list.append((t,p,i))

ans = [0]
def bfs(day,pay,index): #필요한 일수, 받을 금액, 현재 인덱스
    q = deque()
    q.append((day,pay,index))
    while q:
        d,p,idx = q.popleft()
        ans.append(p)
        for i in range(idx+d,n): #현재 인덱스+일수부터 상담 가능
            if i+consult_list[i][0]-1<n: #상담이 끝나는 날짜가 n보다 작은 경우만 추가 상담 가능
                q.append((consult_list[i][0],p+consult_list[i][1],i)) #받을 금액 누적시키기

for x in range(n):
    if x+consult_list[x][0]-1<n: #상담이 끝나는 날짜가 n보다 작은 경우만 bfs
        bfs(consult_list[x][0],consult_list[x][1],x)
# print(ans)

print(max(ans))
