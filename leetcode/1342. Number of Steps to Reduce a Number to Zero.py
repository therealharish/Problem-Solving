class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        while (num):
            c+=1
            if(num%2==0):
                num = num//2
            else:
                num = num - 1
        return c