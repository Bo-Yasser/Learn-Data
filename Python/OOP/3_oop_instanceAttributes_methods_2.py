


class Member:

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        
        self.gender = gender
    
    def full_name(self):

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

member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "MALE")
member_three = Member("Mona", "Ali", "Mahmoud", "FEMale")


print(member_one.full_name())
print("#"* 50)

print(member_one.name_with_title())
print(member_three.name_with_title())
print("#"* 50)

print(member_one.get_all_info())
print(member_three.get_all_info())
print("#"* 50)
