email = "mohamed.yasser00@raptor.com"

#print(email[email.index("m"):7])

theName = input("What Is Your Name : ").capitalize().strip(" #$@!%^&*")
theEmail = input("What Is Your Email : ").strip(" !@#$%^&*")

theUsername = theEmail[0:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@") +1:].strip(" !@#$%^&*")

print(f"Hello {theName} Your Email Is {theEmail}")

print(f"Your User Name Is {theUsername} \nAnd Your Website is {theWebsite}.com")