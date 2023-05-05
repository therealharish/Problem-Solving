https://medium.com/basecs/k%C3%B6nigsberg-seven-small-bridges-one-giant-graph-problem-2275d1670a12

https://medium.com/basecs/demystifying-depth-first-search-a7c14cccf056

t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  m = min(arr)
  count=0
  for i in arr:
    count+=(i-m)
  print(count)