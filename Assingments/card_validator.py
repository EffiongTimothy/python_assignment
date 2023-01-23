
    user_input = input("enter card number for validity check ")


def card_type(firstNumber):
    first_number = int(str(firstNumber)[0])
    second_number = int(str(firstNumber)[1])
    if firstNumber.startswith("4"):
        return "visa"
    elif firstNumber.startswith("5"):
        return "MasterCard"
    elif firstNumber.startswith("37"):
        return "AmericanExpress"
    elif firstNumber.startswith("6"):
        return "DiscoveryCard"
    else:
        return "card is unknown"


def length_of_card_number(number_length):
    length_of_number = len(number_length)
    if length_of_number < 13 or length_of_number > 16:
        return "card length is invalid"
    else:
        return length_of_number


def even_double_digits(card_number):
    total_sum_of_even_digits = 0
    for i in range(len(card_number) - 2, -1, -2):
        sum_even = int(card_number[i]) * 2
        if sum_even > 9:
            new_sum = sum_even % 10 + sum_even // 10
            total_sum_of_even_digits += new_sum
        else:
            total_sum_of_even_digits += sum_even
    return total_sum_of_even_digits


def odd_digits(credit_card_number):
    total_odd = 0
    for i in range(len(credit_card_number) - 1, -1, -2):
        total_odd += int(credit_card_number[i])
    return total_odd


result_of_digits = odd_digits(user_input) + even_double_digits(user_input)
if result_of_digits % 10 == 0:
    print("Card is valid")
else:
    print("Card is invalid")


def length_of_line():
    for i in range(70):
        print("#", end="")


length_of_line()
print("\n********* the type of card is " + card_type(user_input))
print("********* the length of the card number is " + str(length_of_card_number(user_input)))
length_of_line()
