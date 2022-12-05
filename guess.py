import random
number_to_be_guessed = random.randint(1, 100)
number_of_guesses = 1

while number_of_guesses <= 3:
    guess = int(input("guess a number between 1 and 100 "))
    if guess == number_to_be_guessed:
        print("you get it right")
        break
    else:
        print("wrong guess try again.")

    if number_of_guesses == 3:
        print("try again later, its unfortunate you could not guess", number_to_be_guessed)

    number_of_guesses += 1


