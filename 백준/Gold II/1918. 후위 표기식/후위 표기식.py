string = input()

stack = []
res = ''
for i in string:

    if i.isalpha():
        res += i

    elif i == '(':
        stack.append(i)
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            res += stack.pop()
        stack.append(i)

    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(i)

    # 괄호가 나올 때까지 스택 비우기
    elif i == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()  # ( 괄호 제거

while stack:
    res += stack.pop()
print(res)