min_num, max_num = map(int, input().split())
chk = [1]*(max_num-min_num+1)
p = 2
while p < int(max_num**0.5)+1:
    temp_idx = (p**2 - min_num % p**2) % p**2
    while temp_idx < max_num-min_num+1:
        chk[temp_idx] = 0
        temp_idx += p**2
    p += 1
print(sum(chk))