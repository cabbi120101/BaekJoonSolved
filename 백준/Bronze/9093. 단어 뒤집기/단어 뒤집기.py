T = int(input())
for tc in range(1,T+1):
    string = ' '.join(map(lambda x:x[::-1],input().split()))
    print(string)