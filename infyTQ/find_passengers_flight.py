#lex_auth_0127382193364008961449

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
  count =0;
  for i in ticket_list:
    string_list=i.split(":")
    if(string_list[2]==destination):
      count+=1
  return count
      
    #Write the logic to find and return the number of passengers traveling to the specified destination
    #Remove pass and write your logic here

def find_passengers_per_flight():
  d={}
  l=[]
  for i in ticket_list:
    string_list=i.split(":")
    if (string_list[0] in list(d.keys())):
      d[string_list[0]]+=1;
    else:
      d[string_list[0]]=1;

  for x,y in d.items():
    s = str(x)+":"+str(y)
    l.append(s)
  
  return l
    
  
      

def sort_passenger_list():
  l=find_passengers_per_flight()
  l2=[]
  l4=[];
  for i in l:
      l2.append(i[-1])
  l3=sorted(l2,reverse=True)
  for i in l3:
      for x in l:
          if x[-1]==i:
              l4.append(x)
  return l4
        

    
  
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    #Remove pass and write your logic here

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())