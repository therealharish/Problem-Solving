#lex_auth_0127426391777280001519

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

#Implement Game class here
class Game:
  def __init__(self, players_list):
    self.__players_list = players_list

  def sort_players_based_on_experience(self):
    self.__players_list.sort(reverse = True, key = lambda x: x.get_experience())

  def shift_player_to_new_position(self, old_index_position, new_index_position):
    # self.__players_list[old_index_position-1], self.__players_list[new_index_position-1] = self.__players_list[new_index_position-1], self.__players_list[old_index_position-1]

    
    # temp = self.__players_list[old_index_position-1]
    # for i in range(old_index_position, new_index_position):
    #   self.__players_list[i-1] = self.__players_list[i]

    # self.__players_list[new_index_position-1] = temp

    temp=self.__players_list.pop(old_index_position)
    self.__players_list.insert(new_index_position,temp)


  def display_player_details(self):
    for i in self.__players_list:
      print(i.get_name(), i.get_experience())

  

player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
obj = Game(players_list)
obj.display_player_details()
obj.shift_player_to_new_position(2,5)
print("After Swapping")
obj.display_player_details()
#Create object of Game class, invoke the methods and test your program