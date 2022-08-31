class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
      xor = 0
      xor2=0
      for i in nums:
        xor^=i
      pos = 0
      # Method 1
      # copy = xor
        
      # while(copy):
      #   if(copy&1==0):
      #       pos+=1
      #       copy = copy>>1
      #   else:
      #       break
            
      # for j in nums:
      #   check = 1<<pos
      #   if(j&check):
      #       print(j)
      #       xor2^=j
      # return [xor2^xor, xor2]

      # Method 2, here we find the first differentiator of bits and then find the rest of the xor with it's help as follows

      diff = xor&(-xor)

      for i in nums:
        if(i&diff):
          xor2^=i
      return [xor2, xor2^xor]
              
            