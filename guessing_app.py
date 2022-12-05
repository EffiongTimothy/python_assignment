#count = 3
lucky_number = 50
user_input = input("welcome\npress OK to continue\n")
print("Guess ME :)\n")
print("Hi dear can you guess my lucky number? \n the rule is simple just guess a number between 0--100")
print(" ")
print("hello " + input("Enter player name: \n"), " are you ready?")

print("you only have 3 trials\n")

for count in range(1, 3, 1):
    user_input = int(input("Hey!!! guess my lucky number between 0 to 100 \n"))
    if user_input == lucky_number:
        print("my lucky number is ", lucky_number, " congratulation ....!")
        break
    elif user_input > lucky_number:
        print("oops! the number", user_input, "you entered is higher than my lucky number  try again")

    else:
        print("the number you entered is below my lucky number     keep trying...")
    print(" ")
    if count == 1:
        print("you've used all your trials start again ")
 #   count -= 1
