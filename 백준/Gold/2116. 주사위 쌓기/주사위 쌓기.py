N = int(input())
dice_list = [list(map(int, input().split())) for _ in range(N)]

# 주사위 값 인덱스
across_dict = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}

def chk_max(num):
    res = 0
    for i in range(N):
        for j in range(6):
            if dice_list[i][j] == num:
                other_side = dice_list[i][across_dict[j]]
                # 6이 위 아래면에 있는 경우, 4,5가 최대
                if 6 in [num, other_side]:
                    res += 4 if 5 in [num, other_side] else 5
                else: # 아니면 6
                    res += 6
                num = other_side
                break
    return res

ans = 0
for i in range(1, 7):
    ans = max(ans, chk_max(i))

print(ans)