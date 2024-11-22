


class Food: #Base Class

    def __init__(self, name, price):
        self.name = name
        self.price = price

        print(f"{self.name} Is Created From Base Class")

    def eat(self):

        print("Eat Method From Base Class")






class Apple(Food): #Drived Class
    
    def __init__(self, name, price, amount):
        self.list = [1, 2, 3, 4]
        # Food.__init__(self, name, price)
        
        
        super().__init__(name, price)
        
        # self.name = name
        # self.price = price + 20
        self.amount = amount
        print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")

    def __str__(self):

        print("Str Method Is Amazing")
    def __len__(self):

        return len(self.list)
    
    def get_from_tree(self):

        print("Get From Tree From Derived Class")    

    # def eat(self):                         # Method Override

    #     print("Eat Method From Base Class")



# food_one = Food("Pizza", 10)
food_two = Apple("Pizza", 150, 500)        
print("#"*50)

food_two.eat()
food_two.get_from_tree()
Apple.get_from_tree(food_two)                    # not make new instance
# Apple.get_from_tree(Apple("Pizza", 150, 500))  # make new instance
# print("#"*50) 





# Apple.__str__(food_two)
# print(len(food_two))
# food_two.list.append("ZaZa")
# print(len(food_two))
# print("#"*50) 

# print(Apple.mro())