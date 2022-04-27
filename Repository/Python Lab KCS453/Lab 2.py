print("Enter size of first matrix: ")
x,y = map(int, input().split())
print("Enter size of second matrix: ")
a,b = map(int, input().split())

if(y!=a):
  print("Multiplication not Possible")
else:
  arr1 = [[0]*y for i in range(x)]
  arr2 = [[0]*b for i in range(a)]

  print("Enter elements of first matrix: ")
  for i in range(x):
    for j in range(y):
      arr1[i][j]=int(input())

  print("Enter elements of second matrix: ")
  for i in range(a):
    for j in range(b):
      arr2[i][j]=int(input())
      
  c = [[0]*b for i in range(x)]
  for i in range(x):
    for j in range(b):
      for k in range(a):
        c[i][j]+= arr1[i][k] * arr2[k][j]
  print(c)

                                                                                                                                                                                                                                                         