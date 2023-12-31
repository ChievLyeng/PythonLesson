def solve(S) :
    open = "[{("
    close = "]})"
    stack = []

    for s in S :
        if s in open :
            stack.append(s)
            print("stack :",stack)
        elif stack and open.index(stack[-1]) == close.index(s) : 
            print("B",stack[-1])
            stack.pop()
        else :
            return False
    return len(stack) == 0

S = input()
print("Yes" if solve(S) else "No")