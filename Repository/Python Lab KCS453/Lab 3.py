from math import gcd

print("Enter two numbers: ")
a,b = map(int, input().split())

print(gcd(a,b))