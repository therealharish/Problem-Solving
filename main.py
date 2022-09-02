s = "moomso"
n = len(s)
l = [[s[k] for k in range(n) if i&1<<k] for i in range(2**n)]
check = []


def checkPalindrome(test):
  if(test == test[::-1]):
    return True

for i in l:
  if i:
    check.append("".join(i))

maxLen = 0
result = ""
for i in check:
  if(checkPalindrome(i) and maxLen<len(i)):
    maxLen = len(i)
    result = i

print(result)



