N = 9
arr = [int(input()) for _ in range(9)]
cha = sum(arr) - 100
arr.sort()
for i in arr:
    try:
        if i == cha-i:
            pass
        else:
            arr.remove(cha - i)
            arr.remove(i)
            break
    except:
        pass
for j in arr:
    print(j)