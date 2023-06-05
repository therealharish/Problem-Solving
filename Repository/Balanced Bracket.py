t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    def balancedBrackets(s):
        stack = []
        count = 0
        flag = 0
        for i in s:
            if i == '(':
                stack.append(i)
                flag = 1
            else:
                if len(stack) == 0:
                    return False
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                    if flag:
                        count += 1
                        flag = 0
        return count
    
    print(balancedBrackets(s))