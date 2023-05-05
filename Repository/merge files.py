# Program 1
# f1 = open("Repository/txtfiles/file1.txt")
# s1 = f1.read()
# f1.close()

# f2 = open("Repository/txtfiles/file2.txt")
# s2 = f2.read()
# f2.closed

# f3 = open('Repository/txtfiles/file3.txt', 'w')
# s=s1+s2
# f3.write(s)
# f3.close()


# ---------------------------------------------
#Program 2
# f1 = open("Repository/txtfiles/file1.txt")
# s1 = f1.readlines()
# f1.close

# f2 = open("Repository/txtfiles/file2.txt")
# s2 = f2.readlines()
# f2.closed

# l = []
# i=0
# j=0

# while i<len(s1) and j<len(s2):
#   l.append(s1[i])
#   l.append(s2[j])
#   i+=1
#   j+=1

# f3 = open('Repository/txtfiles/file3.txt', 'w')
# f3.writelines(l)
# f3.close()


# # ---------------------------------------------
# #Program 3
# f1 = open("Repository/txtfiles/file1.txt")
# s  = f1.read()
# f1.seek(0)
# s1 = f1.readlines()
# print("No. of characters: ", len(s))
# count=0
# for i in s1:
#   count+=1
# print("No. of Words: ", count)
# print("No. of Lines: ", len(s1))
# f1.close()


# # ---------------------------------------------
# #Program 4
# f1 = open("Repository/txtfiles/file1.txt")
# s1 = f1.readlines()
# print("First Line: ", s1[0])
# print("Last Second Line: ", s1[-2])
# f1.close()


# # ---------------------------------------------
# #Program 5
with open("Repository/txtfiles/file1.txt") as f:
  s1 = f.readlines()
  print(s1)
  d = {}
  for i in s1:
    if(i.count(" ")>1):
      for j in i.split():
        if j in d:
          d[j]+=1
        else:
          d[j] =1
    else:
      if i in d:
        d[i]+=1
      else:
        d[i]=1
  print(d)
  print(max(d, key = d.get))
    