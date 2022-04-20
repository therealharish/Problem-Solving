class Solution:
    
    
      
    def generate(self, numRows: int) -> List[List[int]]:
        lis=[]

        def retlist(num, rows):
          l = []
          for i in range(rows):
            for j in range(0, i+1):
              if(j==0 or i==0):
                co = 1
              else:
                co = co+(i-j+1)//j
            l.append(co)
                
          return l 

        
      
        for i in range(0,numRows):
          lis.append(retlist(num, i))
        
        return lis


    
      
