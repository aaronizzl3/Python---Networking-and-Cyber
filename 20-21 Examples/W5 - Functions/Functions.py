
# TODO: Function Syntax


def myFunction():
    print("Function One.")
    myFunction2()


def myFunction2():
    print("Function Two.")


# TODO: Addition
def Addition():
    numA = int(input("Enter first number: "))
    numB = int(input("Enter second number: "))
    print(f"{numA} + {numB} = {numA + numB}")


# TODO: Student Profile (Arguments)
def Student(name, age, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")


# TODO: Sum of two numbers (Return)
def Sum(a, b):
    answer = a + b
    return answer

# TODO: Function Calls
#Addition()
#Student("Joe Bloggs", 21, "Advanced Pottery")
#Student("Miss Fantastic", 1000, "Beating Up Bad Guys")
#Student(input("Name: "), int(input("Age: ")), input("Course: "))

x = Sum(5, 10)
print(x * 2)
