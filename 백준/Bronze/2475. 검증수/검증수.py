num_list = [i**2 for i in list(map(int, input().split()))]
print(sum(num_list)%10)