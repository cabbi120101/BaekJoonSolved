import sys

input = sys.stdin.readline

n = int(input())
max_j = 0
max_table = []
for i in range(n,n//2,-1): #절반 이상일동안 값을 하나씩 줄이며 규칙 수행
    table = [0]*30000
    table[0] = n
    table[1] = i
    table[2] = n-i
    j = 3
    while True:
        table[j] = table[j-2]-table[j-1]
        if table[j] < 0:
            break
        if j>max_j: #최대개수인지 확인
            max_j = j
            max_table = table
        j += 1
print(max_j+1)
print(' '.join(map(str,max_table[:max_j+1])))