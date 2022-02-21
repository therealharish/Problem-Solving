
# def check(a,b):
#   count=1;
#   m=0;
#   k=[0]
#   m=[0]
#   i=0;
#   x=0
#   while(i<len(a)):
#     if(m[x]<a[i]):
#       for j in range(len(k)):
#         if(k[j]==0):
#           print("The train arrived at", a[i],"on platform", k[j]);
#           m[x]=b[i]
#           k[j]=1
#           i+=1;
#           x=0
#           break;
#     count+=1;
#     k.append(1)
#     x++;
#     m[x]=a[i];
  
      
      
      
      
      

# a=[2.00, 3.10]
# b=[2.10, 3.50]
# check(a,b)

# def prod(a):
#   f=1;
#   for i in a:
#     f*=i
#   return f

# l = list(map(int, input().split()))
# a=[]
# for i in range(len(l)):
#   left = l[0:i]
#   right = l[i+1:];
#   a.append(prod(left)*prod(right))
# print(a)

l = list(map(int, input().split()))
zero = l.count(0)
one = l.count(1)
ne = "0"*zero
ne+="1"*one
print(ne)

  
  