N = str(input())
N_int = int(N)
ans = 0
start = N_int - (9*len(N)) if (N_int - (9*len(N)) > 0) else 0

for i in range(start, N_int-1):
    temp = i
    for j in str(i):
        temp += int(j)
    if temp == N_int:
        ans = i
        break
print(ans)
