#중위표기법을 후위표기법으로 변경

#우선순위 1(), 2 */, 3 +-
#우선순위 낮은걸 만나면 pop
#)를 만나면 (가 보일때까지 pop


statement = list(input())
stack = []
ans = []

for s in statement:
    if s == '(':
        stack.append(s) #push
        
    elif s == '+' or s == '-': 
        while stack:
            if stack[-1] == '(':
                break 
            else:
                ans.append(stack.pop())
        stack.append(s) #push
        
    elif s == '*' or s == '/': 
        while stack:
            if stack[-1] == '*' or stack[-1] == '/':
                ans.append(stack.pop())
            else:
                break
        stack.append(s) #push
        
    elif s == ')':
        while stack:
            if stack[-1] == '(':
                stack.pop()
                break 
            else:
                ans.append(stack.pop())
    else:
        ans.append(s)

while stack:
    ans.append(stack.pop())
        
print(''.join(ans))
        
