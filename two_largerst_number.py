count = 0
first_number = float("-inf")
second_number = float("-inf")

while count < 5:
    num = float(input("give me a number:\n "))
    if num > first_number:
        second_number = first_number
        first_number = num

    if second_number < num < first_number:
        second_number = num
        second_number = first_number
    count += 1

print("the largest number is: ", first_number, "\n largest number is", second_number)
