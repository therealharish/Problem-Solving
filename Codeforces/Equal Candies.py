t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  m = min(arr)
  count=0
  for i in arr:
    count+=(i-m)
  print(count)