count = 0
largest_number = float("-inf")
smallest_number = float("+inf")
while count != 1:
    user_input = float(input("Enter  number \npress '0' to End input:\n"))
    
    if user_input == 0:
        break
    if user_input > largest_number:
        largest_number = user_input

    if user_input < smallest_number:
        smallest_number = user_input

print("largest number is ", +largest_number)
print("smallest number is ", +smallest_number)
