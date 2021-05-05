import random
user_input = int(input("Guess a number: "))
print(user_input)

magic_number = random. randint (0,10)

if user_input == magic_number:
    print("You Got It!!!")
else:
    print("BZZZZZ Wrong!!! It was %d" % (magic_number))
