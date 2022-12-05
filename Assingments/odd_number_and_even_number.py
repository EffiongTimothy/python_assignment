count = 0
number_odd_number = 0
number_even_number = 0
sum_of_odd_number = 0
sum_of_even_number = 0
while count !=-1:
    user_input = int(input(" Enter a number, enter any negative number to exit\n"))
    if user_input < -0:
        break
    if user_input % 2 == 0:
        number_odd_number +=1
        sum_of_odd_number += user_input
    else:
        number_even_number +=1
        sum_of_even_number += user_input
print("number of odd number entered is ", +number_odd_number)
print("number of even number is ", number_even_number)
print("sum of odd number is ", sum_of_odd_number)
print("sum of even number is ", sum_of_even_number)
