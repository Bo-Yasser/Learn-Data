

def say_hello(name, age) : return f"Hello {name} Your Age Is {age}"

hello = lambda name, age : f"Hello {name}  Your Age Is {age}"


print(say_hello("Ahmed", 36))

print(hello("Ahmed", 36))




print(say_hello.__name__)

print(hello.__name__)


print(type(hello))