import sys
input = sys.stdin.readline

def paper(row, col, n):
    global num_a, num_b, num_c
    save = arr[row][col]
    for i in range(n):
        for j in range(n):
            if arr[row+i][col+j] != save:
                for r in range(3):
                    for c in range(3):
                        paper(row + r * n // 3, col + c * n // 3, n // 3)
                return
    if save == -1:
        num_a += 1
    elif save == 0:
        num_b += 1
    else:
        num_c += 1
    return 


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

num_a, num_b, num_c = 0, 0, 0

paper(0, 0, N)

print(num_a)
print(num_b)
print(num_c)