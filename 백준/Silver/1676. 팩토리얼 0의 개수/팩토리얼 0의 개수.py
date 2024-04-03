N = int(input())

result = 1
for i in range(N):
    result *= (N-i)
# print(result)

reverse_num = str(result)[::-1]
# print(reverse_num)

count = 0
# print(len(reverse_num))
# print(reverse_num[2]) # 근데 왜 여기는 인식해
# print(type(reverse_num[2]))

for i in range(len(reverse_num)):
    if reverse_num[i] == '0':       # 여기서 안됬네
        count += 1
    else:
        break

print(count)