def card_type(firstNumber):
    first_number = int(str(firstNumber)[0])
    second_number = int(str(firstNumber)[1])
    if first_number == 4:
        print("visa")
    elif first_number == 5:
        print("Mastercard")
    elif first_number == 6 and second_number == 7:
        print("AmericanExpress")
    else:
        print("card is unknown")


def length(number_length):
    length_of_number = len(number_length)
    if length_of_number < 13 or length_of_number > 16:
        print("card length is invalid")
    else:
        print(length_of_number)


user_input = input("enter card number for validity check")
for i in range(1,20,1):
    print("#")

card_type(user_input)
length(user_input)
