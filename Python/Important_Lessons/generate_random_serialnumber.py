import string
import random

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

def make_serial(count):

    all_char = string.ascii_letters + string.digits
    # print(all_char)

    chars_count = len(all_char)
    # print(chars_count)
    serial_list = []

    while count > 0:
        random_num = random.randint(0, chars_count - 1)
        
        random_char = all_char[random_num]
        
        serial_list.append(random_char)
    
        count -= 1
    print("".join(serial_list))

make_serial(50)