



class Member:

    not_allowed_users = ["Shit", "Hell", "Baloot"]
    users_num = 0
    
    @classmethod
    def show_users_count(cls):
        print(f"We Have {cls.users_num} Users In Our System")

    @staticmethod
    def static():
        print("Hello From Static Method")    

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        
        self.gender = gender
        
        
        Member.users_num += 1 

    def full_name(self):
        if self.fname in Member.not_allowed_users :
            raise ValueError("Name Not Allowed")
        else:
            return f"{self.fname} {self.mname} {self.lname}"

    
    def name_with_title(self):
        self.gender = self.gender.lower()
        if self.gender == "male":
            
            return f"Hello Mr {self.fname}"
        
        elif self.gender == "female":

            return f"Hello Miss {self.fname}"
        else:
            return f"Hello {self.fname}"
    
    def get_all_info(self):
        return f"Hello {self.name_with_title()}, Your Full Name Is: {self.full_name()}"

    def delete_user(self):
        Member.users_num -= 1
        return f"User {self.fname} Is Deleted."
# print(dir(Member))
print(Member.users_num)
member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "MALE")
member_three = Member("Mona", "Ali", "Mahmoud", "FEMale")
member_four = Member("Shit", "Hell", "Metal", "DD")
print(Member.users_num)
print(member_four.delete_user())
print(Member.users_num)



print("#"* 50)

# print(member_one.get_all_info())

# print(member_four.get_all_info())


Member.show_users_count()
print(member_one.full_name())
print(Member.full_name(member_one))
print(Member.full_name(Member("Osama", "Mohamed", "Elsayed", "Male")))

Member.static()



