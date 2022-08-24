n = int(input())
arr = list(map(int, input().split()))
x=0
for i in arr:
  x^=i
print(x)