import sys
input  = sys.stdin.readline

n = int(input())

an = []
max_h = 0
max_idx = 0
#an에 모든 기둥을 저장하며, 가장 큰 기둥의 위치와 높이를 저장한다.
for i in range(n):
    idx,h = map(int,input().split())
    an.append((idx,h))
    if h>max_h:
        max_h = h
        max_idx = idx
an.sort(key = lambda x:x[0])

points = []
#max값을 기준으로 왼쪽에서는 좌->우로 보며 커지는 기둥을 points에 저장, 오른쪽에서는 우->좌로 보며 커지는 기둥을 points에 저장한다
points.append((max_idx,max_h))
left_max = 0

right_max = 0
i = 0
while an[i][0]<max_idx:
    if an[i][1]>=left_max: #max값이랑 같아도 저장한다
        left_max = an[i][1]
        points.append(an[i])
    i+=1

i = n-1
while an[i][0]>max_idx:
    if an[i][1]>=right_max:
        right_max = an[i][1]
        points.append(an[i])
    i-=1
points.sort(key = lambda x:x[0]) #한번 더 인덱스 기준 정렬

area = 0
for i in range(0,len(points)): #i+1,i-1 주의
    if points[i][0]<max_idx: #max보다 이전에 있는 경우
        area += (points[i+1][0]-points[i][0])*points[i][1]
    if points[i][0]==max_idx: #max인 경우
        area += points[i][1]
    if points[i][0]>max_idx: #max 다음에 있는 경우 
        area += (points[i][0] - points[i-1][0]) * points[i][1]
print(area)
# 7
# 2 4
# 11 4
# 15 6
# 4 10
# 5 3
# 8 10
# 13 9