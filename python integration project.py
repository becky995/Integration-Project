"""
This is my main file for this program
__author__ = Becky Perez
"""

name = input("What is your name?")
print("Hello,", name)
tos = int(input("Would you like a sticker or a t-shirt? (Enter 1 for "
            "sticker, 2 for t-shirt)"))
input_is_bad = True
while input_is_bad:
    try:
        quantity = int(input("Enter the amount of products you would like "
                             "as a whole number (ex. 4):"))
        input_is_bad = False
        print("The amount wanted is:", quantity)
    except ValueError:
        print("This is not a whole number.")
color = (input("What color material would you like?"))
input_is_bad = True
while input_is_bad:
    try:
        length = (input("What is your desire length for image (in inches)? "
                           "Enter as an integer."))
        input_is_bad = False
    except ValueError:
       print("This is not an integer.")
input_is_bad = True
while input_is_bad:
    try:
        width = int(input("What is your desire width for image (in inches)? "
                          "Enter as an integer."))
        input_is_bad = False
        print("The width wanted is:", width)
    except ValueError:
        print("This is not an integer.")
getarea = length * width
print("The desire pruduct is:", quantity,color,tos, getarea)
delivery = int(input("What delivery would you like: enter 1 for standard, "
                     "2 for 3 day shipping, and 3 for 1 day shipping"))
if delivery <= 1:
    print("There is no additional fee.")
elif delivery >= 2:
    print("There is a $3.00 shipping fee.")
else:
    print("There is a $5.00 shipping fee.")