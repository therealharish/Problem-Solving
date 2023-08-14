# inp = input()
# k = int(input())

# def solve(inp, k):
#     s = [int(i) for i in inp]
#     # print(s)
#     ans = ""
#     for i in range(len(s)):
#         ans += str(s[i-k+1])
        
#     return ans
    
    
# print(solve(inp, k))

# function to convert binary to decimal 
def solve(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print(int(binary, 2))

print(solve("1000"))