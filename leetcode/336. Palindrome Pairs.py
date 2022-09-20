class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(s):
            if (s == s[::-1]):
                return True
            else:
                return False

        d = {}
        for i in range(len(words)):
            d[words[i]] = i
        print(d)

        ans = []

        for i in range(len(words)):

            if (words[i] != "" and isPalindrome(words[i]) and "" in d):
                ans.append([i, d[""]])
                ans.append([d[""], i])

            if (not isPalindrome(words[i]) and words[i][::-1] in d):
                ans.append([i, d[words[i][::-1]]])

            for j in range(1, len(words[i])):
                left = words[i][0:j]
                right = words[i][j:]
                if (left[::-1] in d and isPalindrome(right)):
                    ans.append([i, d[left[::-1]]])
                if (isPalindrome(left) and right[::-1] in d):
                    ans.append([d[right[::-1]], i])

        return ans
