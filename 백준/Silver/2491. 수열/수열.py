#2491 수열

N = int(input())
num = list(map(int, input().split()))
# print(num)

max_cnt = min_cnt = 1
result = []
result.append(1)
for i in range(0, N-1):
    if num[i] < num[i+1]:
        max_cnt +=1
        min_cnt = 1
    elif num[i] > num[i+1]:
        min_cnt +=1
        max_cnt = 1
    else:
        max_cnt +=1
        min_cnt +=1
    result.append(max_cnt)
    result.append(min_cnt)

# print(result)
print(max(result))