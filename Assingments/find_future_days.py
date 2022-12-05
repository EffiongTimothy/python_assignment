user_input = int(input("Enter todays's day: "))
input_2 = int(input("Enter the number of days that elapsed since today: "))
input_2 += user_input

if user_input == 0:
    sunday = "sunday"
    print(f"Today is {sunday}  ")
elif user_input == 1:
    monday = "monday"
    print(f"Today is {monday}\t ")
elif user_input == 2:
    tuesday = "Tuesday"
    print("Today is "+tuesday)
elif user_input == 3:
    wednesday = "Wednesday"
    print("Today is "+wednesday)

elif user_input == 4:
    thursday = "Thursday"
    print("Today is "+thursday)

elif user_input == 5:
    friday = "Friday"
    print("Today is "+friday)

elif user_input == 6:
    saturday = "Saturday"
    print("Today is \t"+saturday)

if input_2 == 0:
    sunday = "sunday"
    print(f"and the future day is {sunday} ")
elif input_2 == 1:
    monday = "monday"
    print(f"and the future day is {monday} ")

elif input_2 == 2:
    tuesday = "Tuesday"
    print(f"and the future day is {tuesday} ")

elif input_2 == 3:
    wednesday = "Wednesday"
    print(f"and the future day is {wednesday} ")

elif input_2 == 4:
    thursday = "Thursday"
    print(f"and the future day is {thursday} ")

elif input_2 == 5:
    friday = "Friday"
    print(f"and the future day is {friday} ")

elif input_2 == 6:
    saturday = "Saturday"
    print(f"and the future day is {saturday} ")


