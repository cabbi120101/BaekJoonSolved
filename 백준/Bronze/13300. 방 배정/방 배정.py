import sys

input = sys.stdin.readline

n,k = map(int,input().split())

rooms = [[0]*2 for _ in range(6)] #각 학년별 성별을 담아둔다
ans = 0
for _ in range(n): #학생 수만큼 증가
    s,y = map(int,input().split())
    rooms[y-1][s] += 1

for i in range(6):
    for j in range(2):
        ans += (rooms[i][j]-1)//2 + 1 #각 학년,성별 별로 필요한 방의 수
print(ans)