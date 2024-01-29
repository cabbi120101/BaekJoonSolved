T = int(input())
for _ in range(T):
    a = list(input())
    s = 0
    for i in a:
        if i == "(":
            s += 1
        elif i == ")":
            s -= 1
        if s < 0:
            print("NO")
            break
    if s > 0:
        print("NO")
    elif s == 0:
        print("YES")