import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
print(round(sum(arr) / N))
print(arr[(N-1) // 2])

#최빈값
dic = dict()
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
max_count = max(dic.values())
max_dic = [i for i in dic if dic[i] == max_count]

if len(max_dic) > 1:
    print(max_dic[1])
else:
    print(max_dic[0])

print(arr[-1]-arr[0])