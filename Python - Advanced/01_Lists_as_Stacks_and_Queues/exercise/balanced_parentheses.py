expression = input()
stack = []

for parentheses in expression:
    if parentheses in "{[(":
        stack.append(parentheses)
    else:
        if not stack:
            stack.append(parentheses)
            break

        last_paren = stack.pop()
        if parentheses == '}' and last_paren == "{":
            continue
        elif parentheses == "]" and last_paren == "[":
            continue
        elif parentheses == ")" and last_paren == "(":
            continue
        else:
            stack.append(last_paren)
            break

if stack:
    print("NO")
else:
    print("YES")
