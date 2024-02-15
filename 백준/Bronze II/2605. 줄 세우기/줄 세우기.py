N = int(input())
arr = list(map(int, input().split()))
ans = []
for stu, num in enumerate(arr):
    if num == 0:
        ans.append(stu+1)
    else:
        ans.insert(-num, stu+1)
print(*ans)