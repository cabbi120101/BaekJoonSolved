N,M = map(int,input().split())
card = list(map(int,input().split()))
new_card = []
for i in card:
    for j in card:
        for k in card:
            if i !=j and j!=k and i!=k:
                new_card.append(i+j+k)
new_card = sorted(new_card)
ans = [i for i in new_card if i <= M]
print(ans[-1])