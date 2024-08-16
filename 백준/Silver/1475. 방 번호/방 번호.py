N = input()
num = [0]*(11)
for i in N:
    if i == '9' or i == '6':
        if num[9] < num[6]:
            num[9] += 1
        else:
            num[6] += 1
    else:
        num[(int(i))]+=1
print(max(num))