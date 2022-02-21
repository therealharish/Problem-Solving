f= open("Repository/txtfiles/file1.txt")
slist = f.readlines();  
listofdict = list();

for i in slist:
  l = i.split();
  datadic = dict();
  datadic["roll"] = l[0];
  datadic["name"] = l[1];
  datadic["location"] = l[2];
  listofdict.append(datadic);

print(listofdict)
print("Number of records: ", len(listofdict))

f.seek(0);
data = input("Enter roll number for searching: ")
search = f.read(3)
if(search == data):
  print()

