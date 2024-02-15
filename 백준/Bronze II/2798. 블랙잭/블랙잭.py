N,M = map(int,input().split())
card = list(map(int,input().split()))
new_card = 0
for i in card:
    for j in card:
        for k in card:
            if i !=j and j!=k and i!=k:
                sum_card = i+j+k
                if sum_card > M:
                    continue
                else:
                    if sum_card > new_card:
                        new_card = sum_card

print(new_card)