def check(arr):
  for a in range(len(arr)):
    for b in range(a, len(arr)):
      for c in range(b, len(arr)):
        d = a^b^c
        if(d in arr):
          return True
          
  return False


n = int(input())
arr = list(map(int, input().split()))
if (n>130):
  print(True)
else:
  print(check(arr))


  