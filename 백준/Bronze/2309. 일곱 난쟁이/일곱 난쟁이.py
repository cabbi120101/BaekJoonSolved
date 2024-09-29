nan = [int(input()) for i in range(9)]
nan.sort()
target = sum(nan) - 100
for i in range(9):
    for j in range(i,9):
        if nan[i]+nan[j] == target:
            nan.pop(i)
            nan.pop(j-1)
            break
    if len(nan) == 7:
        break
for i in nan:
    print(i)