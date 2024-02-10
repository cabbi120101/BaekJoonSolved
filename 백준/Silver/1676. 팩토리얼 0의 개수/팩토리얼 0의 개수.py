def find_five(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt
N = int(input())
print(find_five(N))