def clearbitsbetweeniandj(n, i , j):
  m1 = -1 << (i+1)
  m2 = 2**j -1
  mask = m1 | m2
  return n & mask

n = 31
i = 3
j = 1
print(clearbitsbetweeniandj(n, i, j))