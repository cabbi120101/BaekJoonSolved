n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

def check_paper(matrix, x, y, size):
    # 첫 번째 값을 기준으로 모든 값이 같은지 확인
    first_value = matrix[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != first_value:
                return False
    return True

def count_paper(matrix, x, y, size, counts):
    # 만약 현재 종이가 모두 같은 숫자라면 카운트
    if check_paper(matrix, x, y, size):
        counts[matrix[x][y] + 1] += 1
    else:
        new_size = size // 3
        for i in range(3):
            for j in range(3):
                count_paper(matrix, x + i * new_size, y + j * new_size, new_size, counts)



counts = [0, 0, 0]

count_paper(matrix, 0, 0, n, counts)

print(counts[0]) 
print(counts[1])  
print(counts[2]) 
