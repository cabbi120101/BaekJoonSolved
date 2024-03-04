def chk(orders, wheels):
    ans = 0
    for num, dir in orders:
        move = [0] * 4
        move[num - 1] = dir

        for i in range(num - 2, -1, -1):
            if wheels[i + 1][-2] != wheels[i][2]:
                move[i] = -move[i + 1]
            else:
                break

        for i in range(num, 4):
            if wheels[i - 1][2] != wheels[i][-2]:
                move[i] = -move[i - 1]
            else:
                break

        for idx, way in enumerate(move):
            if way == 1:
                last = wheels[idx].pop()
                wheels[idx] = [last] + wheels[idx]
            elif way == -1:
                first = wheels[idx].pop(0)
                wheels[idx].append(first)

    for i in range(4):
        if wheels[i][0] == 1:
            ans += 2 ** i
    return ans


wheel = [list(map(int,list(input()))) for _ in range(4)]
K = int(input())
order = [list(map(int, input().split())) for _ in range(K)]
print(chk(order, wheel))