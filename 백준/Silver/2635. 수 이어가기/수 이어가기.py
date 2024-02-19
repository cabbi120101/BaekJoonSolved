T = int(input())
max_num = 0
ans = []
def suu(num,num1):
    if num-num1 < 0:
        return [num] + [num1]
    else:
        return [num] + suu(num1,num-num1)
for i in range(T,0,-1):
    tmp = suu(T,i)
    if len(tmp) > max_num:
        max_num = len(tmp)
        ans = tmp
    elif len(tmp) < max_num:
        break
print(max_num)
print(*ans)