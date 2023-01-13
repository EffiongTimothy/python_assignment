from Person import Person

if __name__ == '__main__':
    name = input("enter your name")
    age = int(input("enter your age"))
    variable = Person(name, age)
    print(variable.get_age(),variable.get_name())
