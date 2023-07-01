import sys

def isPalindrome(n):
    s = str(n)
    k, j = 0, len(s) - 1
    while k < j:
        if s[k] != s[j]:
            return False
        k += 1
        j -= 1
    return True

def main():
    pal = []
    for i in range(32770):
        if isPalindrome(i):
            pal.append(i)
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        dp = {}
        for num in a:
            if num in dp:
                dp[num] += 1
            else:
                dp[num] = 1
        
        res = 0
        for num in a:
            for p in pal:
                if (num ^ p) in dp:
                    res += dp[num ^ p]
            
            dp[num] -= 1
        
        print(res)

if __name__ == "__main__":
    main()
