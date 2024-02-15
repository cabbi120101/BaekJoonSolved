import sys

input = sys.stdin.readline

c,r = map(int,input().split())
k = int(input())

direction = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)} #달팽이 방향
board = [[0]*c for _ in range(r)]
#r,c-1,r-1,c-2,r-2,...1,1
path = []
path.append(r)
i = 1
while True: #각 방향별로 이동할 횟수.
#  가로 세로가 다르기 때문에 한쪽이 더 이상 전진할 수 없으면 다른쪽 마지막 전진 후 break
    path.append(c-i)
    if c-i==1:
        path.append(r-i)
        break
    path.append(r-i)
    if r-i==1:
        path.append(c-i-1)
        break
    i+=1
# print(path)


def get_locate(path): #k의 좌표를 반환하는 함수
    now = [r - 1, 0]
    d = 0 #현재 전진 방향을 나타냄
    num = 1 #현재 번호
    for now_path in path:
        dx = direction[d][0]
        dy = direction[d][1]
        for i in range(now_path):
            board[now[0]+dx*i][now[1]+dy*i] = num
            if num==k:
                return now[0]+dx*i,now[1]+dy*i
            num+=1
        d = (d+1)%4
        now[0] += dx*i + direction[d][0] #다음 방향 시작점으로 이동
        now[1] += dy*i + direction[d][1]
    return -1,-1

kx,ky = get_locate(path)
if kx==-1:
    print(0)
else:
    # print(kx,ky)
    print(ky+1,r-kx) # 문제의 요구 좌표로 수정
# for i in range(r):
#     for j in range(c):
#         print(board[i][j])
#         print(j+1,r-i)
