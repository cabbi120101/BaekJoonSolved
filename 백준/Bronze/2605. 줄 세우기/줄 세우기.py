N = int(input())
arr = [i for i in range(1,N+1)]
number = list(map(int, input().split()))
ans = []

for i,stu in zip(number, arr):
    if i == 0:
        ans.append(stu)
    else:
        ans.insert(-i,stu)
print(*ans)