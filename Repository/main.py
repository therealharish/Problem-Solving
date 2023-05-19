import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here

n, x = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse = True)

var = arr[x-1]
c = 0

for i in arr:
    if i >= var:
        c+=1
    else:
        c+=0

ans = -1
if c == x:
    ans = var
else:
    ans = -1
print(ans)



    
    
