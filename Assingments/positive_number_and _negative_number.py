positive_number = 0
negative_number = 0
total = 0
average = 0
user_input = int(input("Enter an integer, the input ends if it is 0: "))
while user_input != 0:
    user_input = int(input())
    if user_input < 0:
        negative_number += 1
    if user_input > 0:
        positive_number += 1
    if user_input == 0:
        print("no number entered except 0")
    else:
        total += user_input
sum_up = positive_number + negative_number
average = total / sum_up
print(f"The number of positive is  {positive_number}")
print(f"The number of negative is {negative_number}")
print(f"The total is  {total}")
print(f"the average {average:.2f}")
