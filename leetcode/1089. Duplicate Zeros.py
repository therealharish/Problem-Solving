class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
      d = [0 for i in range(len(arr))]
      x = 0
      i=0
      while(i<len(arr) and x<len(d)):
        if arr[i]!=0:
          d[x] = arr[i]
        else:
          x+=1
        x+=1
        i+=1
      arr[::] = d
    