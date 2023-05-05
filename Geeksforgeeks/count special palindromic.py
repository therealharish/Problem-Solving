class Solution:

    def CountSpecialPalindrome(self, S):
        s = S
        l = len(s)
        same = [0]*l
        ws = 0
        res = 0
        for we in range(l):
            if(s[ws] == s[we]):
                continue
            else:
                same[ws] = we-ws
                res += ((same[ws])*(same[ws]+1))//2
                ws = we
        same[ws] = l - ws
        res += ((same[ws])*(same[ws]+1))//2
        # print(same)
        for i in range(l):
            if(same[i]==0 and s[i]==s[i-1]):
                same[i]=same[i-1]
        # print(same)
        for i in range(1, l-1):
            if(s[i-1]==s[i+1] and s[i+1]!=s[i]):
                res += min(same[i-1], same[i+1])
        return res-l