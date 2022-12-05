star = "mississippi is the longest river"
print(star[0:21:4])
print(star[27::8])
print(star[-5:])
print(star[::-1])
print(star[12:19])
print(star[-15:-21:-1])
print(star[-21:-13:-1])
a = "spam out"
print(a)
na = a[:2] + "er" + a[3::]
print(na)
b = 2
print(f"soory is this the {5} minute {'ARUGUMRNTS'}")
print(a, " is ", b, "is")
s = f"{a:^2} is {b:>5.5f}"
print(s)
hello = "hello"

for i, l in enumerate(hello):
    print(f"{l} --> {i}")
print()
for index in range(len(hello)):
    print(f"{hello[index]} -->{index}")
for i in range(1,21,2):
  s = "*" * i
  print(f"{s:>20}{s:>20}{s:<20}{s:<20}")