import sys

input = sys.stdin.readline

def counting_sort(an):
    count = [0]*100
    result = [0]*len(an)
    for item in an:
        count[item]+=1
    for i in range(1,100):
        count[i] += count[i-1]
    for i in range(len(an)):
        count[an[i]] -= 1
        result[count[an[i]]] = an[i]
    return result



heights = []
for _ in range(9):
    heights.append(int(input()))

def dfs(idx):
    if len(res):
        return
    if len(s)==7:
        summ = 0
        for item in s:
            summ+=heights[item]
        if summ==100:
            res.extend(list(s))
        return
    for i in range(idx,9):
        if not i in s:
            s.append(i)
            dfs(i)
            s.pop()

s = []
res = []
dfs(0)
res = counting_sort([heights[x] for x in res])
print('\n'.join(map(str,res)))