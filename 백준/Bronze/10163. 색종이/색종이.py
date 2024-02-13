import sys

input = sys.stdin.readline

n = int(input())
board = [[0]*1001 for _ in range(1001)]
for num in range(1,n+1):
    x,y,width,height = map(int,input().split()) #익순한 x,y좌표배열과 다르지만 정사각형이므로 신경쓰지 않는다
    for i in range(x,x+width): #각 색종이 위치에 순서값을 대입한다 (이후에 겹치면 덮에씌워짐)
        for j in range(y,y+height):
            board[i][j] = num

count_area = [0]*(n+1)
for r in range(1001): #평면을 돌며 색종이 순서값 카운트
    for c in range(1001):
        count_area[board[r][c]] +=1
print('\n'.join(map(str,count_area[1:])))