
# 1

class Game:
    
    def __init__(self, name, developer, year, price):

        self.name = name
        self.developer = developer
        self.year = year
        self.price = price
    def price_in_pounds(self):
        return f"{self.price * 48.5} Egyptian Pounds"

# game_one = Game("Ys", "Falcom", 2010, 50)

# print(f"Game Name Is \"{game_one.name}\", ", end="")
# print(f"Developer Is \"{game_one.developer}\", ", end="")
# print(f"Release Date Is \"{game_one.year}\", ", end="")
# print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# Needed Output
# Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds
# Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 2425.0 Egyptian Pounds



# 2

class User:
    def __init__(self, fname, lname, age, gender):

        self.fname = fname
        self.lname = lname
        self.age = age 
        self.gender = gender 
    
    def gender_title(self):
        self.gender = self.gender.capitalize()
        if self.gender == "Male":
            return f"Hello Mr {self.fname} {self.lname:.1}."
        elif self.gender == "Female":
            return f"Hello Mrs {self.fname} {self.lname:.1}."
    
    def full_details(self):

        return f"{self.gender_title()} [{str(40 - self.age).zfill(2)}] Years To Reach 40"




# user_one = User("Osama", "Mohamed", 38, "Male")
# user_two = User("Eman", "Omar", 25, "Female")

# print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
# print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40



# 3 

class Message:
    @classmethod
    def print_message(cls):
        return "Hello From Class Message"

      


# print(Message.print_message())

# Output
# Hello From Class Message




# 4

class Games:

    def __init__(self, game):
        self.game = game

    def show_games(self):
      
      
      if type(self.game) == list or type(self.game) == tuple:
            if len(self.game) > 1:
                print("I Have Many Games:")
                for one in self.game:
                    print(f"-- {one}")
            else:
               print(f"I Have One Game Called \"{self.game[0]}\"")
      elif type(self.game) == str:
            print(f"I Have One Game Called \"{self.game}\"")
               
      elif  type(self.game) == int or type(self.game) == float:
            print(f"I Have {self.game} Game.") 

# my_game = Games("Shadow Of Mordor")
# my_games_names = Games(["Ys II"])
# my_games_count = Games(80)

# my_game.show_games()
# # Ouput
# # I Have One Game Called "Shadow Of Mordor"

# my_games_names.show_games()
# # Ouput
# # I Have Many Games:
# # -- Ys II
# # -- Ys Oath In Felghana
# # -- YS Origin

# my_games_count.show_games()
# # Output
# # I Have 80 Game.




# 5


# Main Class
class Members:

    def __init__(self, n, p):

        self.name = n

        self.permission = p

    def show_info(self):

        return f"Your Name Is {self.name} And You Are {self.permission}"

class Admins(Members):

    pass
        
class Moderators(Members):

    pass



# member_one = Admins("Osama", "Admin")
# member_two = Moderators("Ahmed", "Moderator")

# print(member_one.show_info())
# # Output
# # Your Name Is Osama And You Are Admin

# print(member_two.show_info())
# # Output
# # Your Name Is Ahmed And You Are Moderator



# 6

class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C:

  def __init__(self, three):

    self.three = three



class Text(A, B, C):

    def __init__(self, one, two, three):

        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)

    def show_name(self):
        
        return f"The Name Is {self.one}{self.two}{self.three}"

the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# # Ouput
# The Name Is Elzero