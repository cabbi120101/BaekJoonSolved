C,R = map(int, input().split())
K = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = 0
x,y = 0,0
arr = [[0]*R for _ in range(C)]
num = 2
if K > C*R:
    print(0)
else:
    arr[0][0] = 1
    while num <= K:
        mx = x + dx[d]
        my = y + dy[d]
        if 0<= mx < C and 0<=my<R and arr[mx][my] == 0:
            arr[mx][my] = num
            x,y = mx, my
            if num == K:
                break
            else:
                num += 1
        else:
            d = (d+1)%4
    print(x+1,y+1)