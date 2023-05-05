n = int(input("Enter size of record: "))
d={}
for i in range (n):
  key = input("Name: ");
  value = input("Marks: ");
  d[key] = value;
print(d)
k = list(d.keys());
v = list(map(int, list(d.values())))

maxi = max(v)
i = v.index(maxi)
print("Student with maximum marks is: ", k[i])