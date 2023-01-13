import array

x = [1, 2, 3, 4, 5, "Bolaji"]
x.insert(3, "kenny")
# for inner in x:
#     print(x)
# print(x[1])
# y = array('i', [1, 2, 3, 4, 5])
# print(y)
arr = []
for i in range(5):
    arr.append("hi")
    print(arr, "-->", i)

arr.insert(3, "hello")
# arr.clear()
corn = arr.copy()
print(arr)
print(corn.count("hi"))

set_value = {3}
user_input = input("enter something")
count = 0
for i in range(len(user_input)):
    if user_input[i] != set_value[i]:
        set_value.add(user_input[i])
    else:
        count += 1
    print(user_input[i])
