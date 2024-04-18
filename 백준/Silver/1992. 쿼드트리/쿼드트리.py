def quadtree(row, col, n):
    save = arr[row][col]
    flag = True
    for i in range(n):
        for j in range(n):
            if arr[row+i][col+j] != save:
                print('(', end='')
                quadtree(row, col, n//2)
                quadtree(row, col+n//2, n//2)
                quadtree(row+n//2, col, n//2)
                quadtree(row+n//2, col+n//2, n//2)
                print(')', end='')
                flag = False
                break
        if not flag:
            break
    if flag:
        print(save, end='')


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

quadtree(0, 0, N)