def quadtree(row, col, n):
    save = arr[row][col]
    for i in range(n):
        for j in range(n):
            if arr[row+i][col+j] != save:
                # print('(', end='')
                return '(' + quadtree(row, col, n//2) + quadtree(row, col+n//2, n//2) + quadtree(row+n//2, col, n//2) + quadtree(row+n//2, col+n//2, n//2)  + ')'
                # print(')', end='')
        # print(save, end='')
    return str(save)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

a = quadtree(0, 0, N)
print(a)