def two_point(n, tang):
    left = 0
    max_len = 0
    count = [0] * 10
    one_fruit = 0

    for right in range(n):
        if count[tang[right]] == 0:
            one_fruit += 1
        count[tang[right]] += 1

        while one_fruit > 2:
            count[tang[left]] -= 1
            if count[tang[left]] == 0:
                one_fruit -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

N = int(input())
tang = list(map(int, input().split()))

print(two_point(N, tang))
