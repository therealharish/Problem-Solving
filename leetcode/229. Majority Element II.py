class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
      cd1 = -1
      cd2 = -1
      count1 = 0
      count2 = 0
      for i in nums:
        if(cd1 == i):
          count1+=1
        elif(cd2 ==i):
          count2+=1
        else:
          if(cd1!=i and count1==0):
            cd1 = i
            count1+=1
          elif(cd2!=i and count2==0):
            cd2 = i
            count2+=1
          else:
            count1-=1 
            count2-=1
      
      ans = []
      if(nums.count(cd1)>len(nums)/3):
        ans.append(cd1)
      if(if cd1!=cd2 and nums.count(cd2)>len(nums)/3):
        ans.append(cd2)
      
      return ans