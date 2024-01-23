N = str(input())
N_list = sorted([int(i) for i in N])[::-1]
print(int(''.join([str(i) for i in N_list])))