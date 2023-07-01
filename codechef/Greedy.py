t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    d = ['' for i in range(26)]
    
    ans = 0
    def solve(i, curr, d): 
        global ans
        if ans:
            return
        if i == n:
            # print(curr, validParen(curr))
            if validParen(curr):
                print("Yes")
                print(curr)
                ans = 1
                
        else:
                
            ele = ord(s[i]) - ord('a')
            if d[ele] == '':
                d[ele] = '('
                solve(i + 1, curr + '(', d)
                d[ele] = ')'
                solve(i + 1, curr + ')', d)
                d[ele] = ''
            else:
                solve(i + 1, curr + d[ele], d)
            
    def validParen(s):
        stack = []
        for ele in s:
            if ele == '(':
                stack.append(ele)
            else:
                if not stack:
                    return False
                stack.pop()
        if stack:
            return False
        return True
    
    solve(0, '', d)
    if not ans:
        print("No")
    
        
        
                
        
        
    
    