n = int(input())

F = [0]*22
F[1] = 1
F[2] = 1
flag = 3
while flag <= n:
    F[flag] = F[flag-1] + F[flag-2]
    flag += 1
print(F[n])
