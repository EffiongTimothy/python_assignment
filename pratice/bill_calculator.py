print("welcome to tip calculator\n")
bill = float(input("what was the total bill? $"))
spilt_number = int(input("how many people to slipt the bill? "))
tip = float(input("how many percentage tip would you like to give? "))
balance = bill / spilt_number

result = f"{balance:.1%}"
print(result)
print(type(result))