for i in range(1,15,2):
  s = "*" * i
  print(s.center(30))

hello = "hello there"
print(hello.replace("l","b"))
bin = "101010101001111101118"
print(bin.replace("1", "x").replace("0", "1"))
print(bin.translate(str.maketrans("01","10", "8")))