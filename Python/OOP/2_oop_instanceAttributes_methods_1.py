

class Member:

    def __init__(self, first_name, middle_name, last_name):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name



member_one = Member("Osama", "Mohamed", "Elsayed")
member_two = Member("Ahmed", "Ali", "Mahmoud")
member_three = Member("Mona", "Ali", "Mahmoud")

# print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname, member_two.mname, member_two.lname)
print(member_three.fname, member_three.mname, member_three.lname)
