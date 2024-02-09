T = int(input())
M = 1234567891
r = 31
user = input()
ans = 0
for i in range(T):
    # ord -> ordinal position (문자의 순서 위치 값 -> 반대는 chr())
    # 아스키코드상 a는 97 -> z는 122 (즉, 96을 빼면 1->26고유한 번호 나옴)
    num = ord(user[i]) - 96
    ans += num * (r ** i)
print(ans % M)