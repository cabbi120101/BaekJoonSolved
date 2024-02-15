arr = sorted(int(input()) for _ in range(9))
cha = sum(arr) - 100
for i in arr:
    if i == cha-i:
        pass
    elif cha-i in arr:
        arr.remove(cha - i)
        arr.remove(i)
        break
for j in arr:
    print(j)