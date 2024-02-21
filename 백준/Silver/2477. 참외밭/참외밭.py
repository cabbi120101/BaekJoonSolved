K = int(input())
max_chk = dict()
all_length = []
for i in range(6):
    d, go = map(int, input().split())
    all_length.append(go)
    if d in max_chk:
        del max_chk[d]
    else:
        max_chk[d] = (i,go)
ans = 1
sub = 1
for i in max_chk:
    ans *= max_chk[i][1]
    sub *= all_length[((max_chk[i][0]+3)%6)]
print((ans-sub)*K)