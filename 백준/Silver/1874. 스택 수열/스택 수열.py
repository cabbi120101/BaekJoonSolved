count = 1
temp = True
stack = []
ans = []

N = int(input())
for i in range(N):
    num = int(input())

    while count <= num:
        stack.append(count)
        ans.append('+')
        count += 1
    
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    # 스택 수열을 만들 수 없으므로 False
    else:
        temp = False
        break


if temp == False:
    print("NO")
else:
    for i in ans:
        print(i)
