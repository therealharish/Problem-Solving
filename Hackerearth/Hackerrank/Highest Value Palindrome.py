def highestValuePalindrome(s, n, k):
    # Write your code here

    s1 = list(s[:n // 2])
    s2 = list(s[n // 2:])
    if n % 2:
        l = [s2.pop(0)]
    else:
        l = []
    s2 = s2[::-1]
    i, d = 0, 0
    while i < len(s1):
        if s1[i] != s2[i]:
            d += 1
        i += 1
    # print(d)
    for i in range(len(s1)):
        if d>k:
            return '-1'
        if s1[i]==s2[i]:
            if s1[i]=='9':
                continue
            elif k-2>=d:
                s1[i],s2[i]='9','9'
                k-=2
        elif s1[i]!=s2[i]:
            if s1[i]=='9':
                if k-1>=d-1:
                    s2[i]='9'
                    k-=1
                    d-=1
            elif s2[i]=='9':
                if k-1>=d-1:
                    s1[i]='9'
                    k-=1
                    d-=1
            else:
                if k-2>=d-1:
                    s1[i], s2[i] = '9', '9'
                    k -= 2
                    d-=1
                elif k-1>=d-1:
                    if s1[i]<s2[i]:
                        s1[i]=s2[i]
                        k-=1
                        d-=1
                    elif s1[i]>s2[i]:
                        s2[i]=s1[i]
                        k-=1
                        d-=1
    if n%2 and k:
        l=['9']
    return ''.join(s1+l+s2[::-1])

if __name__ == '__main__':
    n,k=map(int,input().split())
    s=input()
    print(highestValuePalindrome(s,n,k))
