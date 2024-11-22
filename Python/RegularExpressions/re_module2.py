import re 
# 1

string_one = "I Love Python Programming-Language"

search_one = re.split(r"\s", string_one, 1)

print(search_one)

print("#"* 50)

# 2

string_two = "How-To_Write_A_Very-Good-Article"

search_two = re.split(r"-|_", string_two)

print(search_two)

print("#"* 50)


# 3

for count, word in enumerate(search_two, 1):
    if len(word) == 1:
        continue
    print(f"Word Number: {count} => {word.lower()}")


print("#"* 50)

# 4

print(re.sub(r"\s", "-", "I Love Python", 2))
