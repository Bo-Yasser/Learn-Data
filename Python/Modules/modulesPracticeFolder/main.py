
import my_mod


my_mod.say_hello("Osama")
my_mod.say_welcome("Osama")

print("#"* 50)
from my_mod import say_welcome


say_welcome("Osama")


print("#"* 50)

from my_mod import say_welcome as new_welcome


new_welcome("Osama")