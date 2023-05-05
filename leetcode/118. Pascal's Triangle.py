class Solution:
    
    
      
    def generate(self, numRows: int) -> List[List[int]]:
        lis=[]

        def retlist(rows):
          l = []
          for i in range(rows):
            co=""
            for j in range(0, i+1):
              if(j==0 or i==0):
                co = ""
              else:
                co = co+(i-j+1)//j
            l.append(int(co))
                
          return l 

        
      
        for i in range(0,numRows):
          lis.append(retlist(i))
        
        return lis


    
      
