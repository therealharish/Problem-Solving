class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        l = list(n)
        s = 0
        p = 1
        for i in l:
            s+=int(i)
            p*=int(i)
        return p-s