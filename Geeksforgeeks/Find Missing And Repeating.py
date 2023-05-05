#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 

        
        xor = 0
        for i in arr:
            xor = xor^i
        for i in range(1, n+1):
            xor = xor^i

        pos = 0
        temp = xor
        while(temp&1==0):
            pos+=1
            temp=temp>>1
          
        mask = 1<<pos
        matchset = []
        unmatchset=[]
        for i in arr:
            if(i&mask):
                matchset.append(i)
            else:
                unmatchset.append(i)
        for i in range(n+1):
            if(i&mask):
                matchset.append(i)
            else:
                unmatchset.append(i)
              
        missing = 0
        duplicate = 0
        for i in matchset:
            missing = missing^i
        for j in unmatchset:
            duplicate = duplicate^j
            
            
        if(duplicate not in arr):
          missing, duplicate = duplicate, missing
        return [duplicate, missing]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends