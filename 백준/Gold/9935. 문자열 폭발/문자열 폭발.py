string = input()
PPUNG = list(input())
long = len(PPUNG)
temp = []
for i in string:
    temp.append(i)
    if i == PPUNG[-1]:
        if len(temp) >= long and temp[-long:] == PPUNG:
            del temp[-long:]

print(''.join(temp) if temp else 'FRULA')