# in notes 1 pg 16
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        check = 0
        for i in range(len(data)):
            if(check == 0):
                count=0
                mask=1<<7
                while (data[i]&mask):
                    count+=1
                    mask=mask>>1
                if(count == 0):
                    check = 0
                    continue
                elif(count == 2):
                    check = 1
                    continue
                elif(count == 3):
                    check = 2
                    continue
                elif(count == 4):
                    check = 3
                    continue
                else:
                    return False
            if(check):
                if(data[i]&(10<<6)):
                    check-=1
                else:
                    return False
        if(check == 0):
            return True
        else:
            return False
    
                
            
            

            
            
            