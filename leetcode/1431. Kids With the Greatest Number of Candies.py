class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        for i in range(len(candies)):
            if(candies[i]+extraCandies >= max(candies)):
                l.append(True)
            else:
                l.append(False)
            
        return l
                