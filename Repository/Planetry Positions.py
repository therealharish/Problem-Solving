n, q = map(int, input().split())
s = input()
queries = list(map(int, input().split()))
l = list(s)

tots = 0

for i in range(len(l)-1):
    if l[i] == '0' and l[i+1] == '1':
        tots += 1
    elif l[i] == '1' and l[i+1] == '0':
        tots += 1
    else:
        tots += 2
        

for i in queries:
    i -= 1
    if i == 0:
        if l[i] == '0' and l[i+1] == '1':
            tots += 1
        elif l[i] == '1' and l[i+1] == '0':
            tots += 1
        else:
            tots -= 1  
    elif i == len(l)-1:
        if l[i] == '0' and l[i-1] == '1':
            tots += 1
        elif l[i] == '1' and l[i-1] == '0':
            tots += 1
        else:
            tots -= 1
    else:
        if l[i] == '0' and l[i-1] == '1':
            tots += 1
        elif l[i] == '1' and l[i-1] == '0':
            tots += 1
        else:
            tots -= 1
        if l[i] == '0' and l[i+1] == '1':
            tots += 1
        elif l[i] == '1' and l[i+1] == '0':
            tots += 1
        else:
            tots -= 1  
        
        
    if l[i] == '0':
        l[i] = '1'
    else:
        l[i] = '0'
        
    print(tots)
    


        
    
