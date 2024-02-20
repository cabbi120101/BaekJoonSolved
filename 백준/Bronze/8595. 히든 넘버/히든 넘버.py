N = int(input())
string = input()
temp = ''
ans = 0
for i in string:
    if i.isdigit():
        temp += i
    else:
        if temp:
            ans += int(temp)
            temp = ''
if temp:
    ans += int(temp)
print(ans)