def solve(n,s) :
    stack,operation =[],""
    j = 0
    x = []

    for i in range(1,n + 1) :
        # print("i :",i)
        stack.append(i)
        # print("stack :",stack)
        operation += "+"
        while stack and s[j] == stack[-1] :
            # print("j :",j,"s[j] :",s[j],"stack[-1] :",stack[-1])
            x.append(stack.pop())
            # print(x)
            operation += "-"
            j += 1
    
    return "No" if stack else operation
    
n = int(input())
s = list(map(int,input().split()))

print(solve(n,s))