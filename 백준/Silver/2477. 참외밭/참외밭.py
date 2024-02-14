import sys
from collections import deque
input = sys.stdin.readline

k = int(input())

path = deque()
count_two = [0]*7
for _ in range(6):
    direction,length = map(int,input().split())
    count_two[direction] += 1 #해당 방향이 몇번 나왔는지 확인
    path.append((direction,length))

two = [idx for idx,x in enumerate(count_two) if x==2] #방향이 두번 나온 방향
one = [idx for idx,x in enumerate(count_two) if x==1] #방향이 한개밖에 없는 방향
while path[0][0] in two: #시작점이 빈 밭 중 한점이 되지 않도록 반시계방향 리스트를 회전시킴
    path.append(path.popleft())
    
    
idx = 0 #빈 밭 면적은 two에 포함된 길이가 4인 방향리스트 중 2번째와 3번째 위치의 곱이다 
empty_area = 1 #빈 밭을 구할 면적
total_area = 1 #전체 밭을 구할 면적
for direction,length in path:
    if direction in one: #전체 밭을 구하기 위한 각 변은 방향이 한개짜리인 길이이다
        total_area *= length
    if direction in two: #빈 밭의 2번째, 3번째 변을 구해주기 위함
        idx +=1
    if idx==2 or idx==3:
        empty_area *= length
        if idx==3: #빈 면적을 구했다면 더 이상 구하지 않는다
            idx = 4

print((total_area - empty_area)*k) #참외 총 개수