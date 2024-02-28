def calculate(a,b,cal):
    if cal == 0:
        return a + b
    elif cal == 1:
        return a - b
    elif cal == 2:
        return a * b
    else:
        return int(a/b)

def chk(idx, total):
    global max_num, min_num
    if idx >= N-1:
        if total > max_num:
            max_num = total
        if total < min_num:
            min_num = total
        return
    for i in range(4):
        if calcul[i]:
            calcul[i] -= 1
            chk(idx+1, calculate(total,number[idx+1],i))
            calcul[i] += 1


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    calcul = list(map(int, input().split()))
    number = list(map(int, input().split()))
    calcul_dic = {0:'+',1:'-',2:'*',3:'/'}
    min_num = 1e9
    max_num = -1e9
    chk(0,number[0])
    print(f'#{tc} {max_num - min_num}')