N = int(input())

for i in range(N+1):
    num = list(map(int, str(i)))
    result = sum(num) + i
    if result == N:
        print(i)
        break
    if i == N:
        print(0)