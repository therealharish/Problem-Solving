class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        flag =0
        if(x<0):
            x = -x
            flag = 1
        while(x):
            r = x%10
            num=num*10+r
            x=x//10
        if(flag==1):
            num=-num
            
        if(num>2**31-1 or num<-2**31):
            return 0
        return num
                