def power_optimized(a,b):
  ans = 1
  while(b):
    last = b&1
    if(last):
      ans = ans*a
    a = a*a
    b = b>>1
  return ans

a = 2
b = 3
print(power_optimized(a,b))