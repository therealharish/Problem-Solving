class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]
        l = "1"*len(b)
        b = int(b, 2)
        l = int(l, 2)
        l = l-b
        return l