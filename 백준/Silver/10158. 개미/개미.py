w,h = map(int, input().split())
p,q = map(int, input().split())
time = int(input())

a = (p + time) // w  # 증가하는 부분인지 감소하는 부분인지 확인
b = (q + time) // h  # 증가하는 부분인지 감소하는 부분인지 확인

if a % 2 == 0:  # 해당 값이 증가하는 부분이라면
    x = (p + time) % w
else:  # 해당 값이 감소하는 부분이라면
    x = w - (p + time) % w

if b % 2 == 0:  # 해당 값이 감소하는 부분이라면
    y = (q + time) % h
else:  # 해당 값이 감소하는 부분이라면
    y = h - (q + time) % h

print(x, y)