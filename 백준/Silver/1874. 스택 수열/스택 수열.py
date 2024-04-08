N = int(input())
stack = []
result = []
no = True
now = 1
for i in range(N):
    num = int(input())
    while now <= num:
        stack.append(now)
        result.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        no = False
        break

if not no:
    print('NO')
else:
    for i in result:
        print(i)