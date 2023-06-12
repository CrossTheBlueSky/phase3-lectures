# !/usr/bin/env python3
#The python shebang is used to make a file executable
#To make the file executable run the command chmod +x /path/to/your/script.py
#Lastly, run the file in your terminal as follows: /path/to/your/script.py
#Todo 1: print a simple string and run the file in your terminal using the command python3 <filename> or the executable option
x = "hello world"
print(x)

#Python Package Index
#To install packages use 'pip install package_name'
#Todo 2: Find a pip package from the PyPi library, install the package and use the package to perform a simple task
# https://pypi.org/ 

#Debugging using ipdb
#Todo 3: Debugging the following code using ipdb
# add a set_trace() in the code, and when you are in the ipdb terminal print the x and y variables
import ipdb

x = "Hello"

y="world"
def multiply(a,b):
    print(type(a))
    if type(a) is int and type(b) is int:
        result = a * b
        return result
    else:
        print("Not valid")


print(multiply(10,5))

# x  = '0'
# y = 5
# num = multiply(x,y)
# print(num)

# def addition(a,b):
#     result = a + b
#     ipdb.set_trace()
#     return result

# a = 60
# b = "hello"


# You can also use the python shell and use print statements to debug code
#Todo 4: Create an error in your code and debug the code using the python shell and print statements

#Variables
#Todo 5: Create a variable and assign it to a value
hello_world = "hello world"
hello_world = "No"
print(hello_world)
#Python Data Types
#Todo 6: Create a data type variable

#str
string = "Hello"

#int
integer = "1"

#float
float_number = 1.10

#bool
boolean = False

#None
none_type = None

#list
new_list = [1,2,2,3,3]
new_list.append(10)
new_list[0] = 60
print(new_list)

#Tuple
new_tuple = (1,2,2,3)
# new_tuple[0] = 60
print(new_tuple[0])

#Set
new_set = {1,2,2,3}
set_list = set(new_list)
print(set_list)

str_to_list = list(string)
print(str_to_list)

print(int(integer))

#list

#Dictionary
new_dict = {"a":1,"b":2}
new_dict["c"] = 3
print(new_dict["c"])
#Type Conversion
#Todo 7: Perform type conversion on a data type

#Python Conditionals and Control Flow

#Syntax of Conditionals

#if statement
#if condition:
    #statement if the condition is true
if not boolean:
    print("it is False")

#if/else syntax
#if condition:
#else:


#if/elif/else syntax
if x is 1:
    pass
elif 1 in new_list:
    print("new_list has 1")
elif "d" not in new_dict:
    print("not in new_dict")
#if condition:
#elif:
#elif:
#else:

#Syntax of a ternary
#[option1] if [condition] else [option2]

#Comparison Operators:
# == : Equal to
# != : Not equal to
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to

#Logical Operators
#and, or, not

#Conditionals and Control Flow

#Test if a number is positive
num = 1
if num >0:
    print("pos")
#Test if a string is empty
string = ""
if not string:
    print("string is empty")

#Test if a number is positive or negative using an else


#Test if a number is positve, negative, or zero, using if, elif, and else

#Test if a number is in between two numbers using the and operator

#Test if a number is positive, even, or both

#Test if a string is empty or not

#Todo 8: Create a condition to check a pet's mood using an if/elif/else and a ternary
pet_name = "tracker"
pet_mood = "bnfaiob"
#If "pet_mood" is "Hungry!", "Tracker needs to be fed."
if pet_mood == "Hungry":
    print("Please feed")
elif pet_mood is "Sad":
    print("Give pets")
else:
    print("All good")
#If "pet_mood" is "Whinny ", "Tracker needs a walk"
#In all other cases, "Tracker is all good"

#While Loop
while_check = True
count = 0
test_array = []
while 10 not in test_array:
    count += 1
    test_array.append(count)
    print(count)
    
item_list = ["apple","orange","peach"]
#For Loop and Range
for i in item_list:
    print(i)

<<<<<<< HEAD
for i in range(10):
    print(i)

for i in range(len(item_list)):
    print(item_list[i])

for key,value in new_dict.items():
    print(value)
    print(f"Item is {key}")
# for key in new_dict:
#     print(new_dict[key])

=======
>>>>>>> main
#String Interpolation example
#Todo 9: Move conditional logic from Deliverable 1 into a function (pet_status) so that we may 
# use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
def pet_status(pet_name,pet_mood):
    ipdb.set_trace()
    print(f"Your pet {pet_name} is {pet_mood}")
    pet_mood = "Happy"
    ipdb.set_trace()
    print(f"{pet_name} is now {pet_mood}")

pet_status(pet_name,pet_mood)
#Todo 10: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

#Todo 11: Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"

#Todo 12: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

