def win_chk(num):
    if num == 0:
        return 'D'
    if A.count(num) > B.count(num):
        return 'A'
    elif A.count(num) == B.count(num):
        return win_chk(num-1)
    else:
        return 'B'


T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]
    print(win_chk(4))