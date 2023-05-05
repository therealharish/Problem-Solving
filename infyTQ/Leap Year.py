#lex_auth_012693797166096384149

def checkYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

def find_leap_years(given_year):
    list_of_leap_years=[];
    i = 1;
    while(i<=15):
      if(checkYear(given_year)):
        list_of_leap_years.append(given_year)
        i+=1;
      else:
        given_year+=1
        
    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)