Garo, Sero = map(int, input().split())
N = int(input())
Garo_list = []
Sero_list = []
def len_max(Gs,li):
    max_len = 0
    temp = 0
    li2 = [0]+sorted(li)+[Gs]
    for i in range(1,len(li2)):
        if li2[i]-temp > max_len:
            max_len = li2[i] - temp
            temp = li2[i]
        else:
            temp = li2[i]
    return max_len
for _ in range(N):
    A, B = map(int, input().split())
    if A == 1:
        Garo_list.append(B)
    else:
        Sero_list.append(B)
G = len_max(Garo, Garo_list)
S = len_max(Sero, Sero_list)
print(G*S)