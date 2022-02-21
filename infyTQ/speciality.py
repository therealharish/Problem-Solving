#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    count=[0,0,0]
    for y in patient_medical_speciality_list:
      if(y=='P' or y=='p'):
        count[0]+=1;
      elif(y=='O' or y=='o'):
        count[1]+=1;
      elif(y=='E' or y=='e'):
        count[2]+=1;
      else:
        pass
    maxpos=count.index(max(count))
    if(maxpos==0):
      key='P';
    elif(maxpos==1):
      key="O";
    elif(maxpos==2):
      key="E";
    else:
      pass

    speciality=medical_speciality[key]
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)