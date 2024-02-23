N = input()
L = len(N) - 1
answer = ((int(N) - (10 ** L)) + 1) * (L + 1)
for i in range(L):
    answer += 9 * (10 ** i) * (i + 1)
print(answer)