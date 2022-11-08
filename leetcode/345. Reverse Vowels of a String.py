class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels  = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', "O", 'U')
        low = 0
        high = len(s)-1
        
        while(low<high):
            while(s[low] not in vowels and low<high):
                low+=1
            while(s[high] not in vowels and low<high):
                high-=1
            s[low], s[high] = s[high], s[low]
            low+=1
            high-=1w
        s = "".join(s)
        return s
            