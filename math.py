# import math
# y = (3, 36, 89, 2, 23, 12, 17)
# x = max(y)
# print("This is the maximum value ",x)

# z = min(y)
# print("This is the minimum value", z)

# #lets get square of two numbers
# a = 12
# b = 10
# pwr = a**b
# print("a raised to b is:", pwr)

# c = math.ceil(23.67808)
# print("The ceil method", c)

# k = math.floor(67.855855)
# print("Round down: ",k)

# #Lets get the volume of a cylinder
# #radius is 20, and length 10 >>>metres
# radius = 20
# length = 10
# volume = math.pi * 20 ** 2 * 10
# print("Volume is", volume, "cubic metres")

# #calculate radius of a cylinder whose volume is 1400m3 and 11.3m high
# Volume = 1400
# height = 11.3
# radius = 1400/math.pi * 11.3 ** -2
# print("The radius is:", radius,"m." )

# #Write a program that takes input and multiplies 2 intgers without using the *operator

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# num3 = (num1, num2)
# product = math.prod(num3)
# print("Product =", product)
def printer():
    print("Welcome to Idyangu!Select as service to continue!")
    print("1.New id, \n2.Change details, \n3.Lost Id")
    IdYangu.idyangugreet()

class IdYangu():
    def idyangugreet():
        print("Welcome to Idyangu!Select as service to continue!")
        print("1.New id, \n2.Change details, \n3.Lost Id")
        idoption = int(input("Enter option number : "))
        if idoption == 1:
            idyangugreet()
        elif idoption == 2:
            changedetails()
        elif idoption == 3:
            lostid()
        else:
            print("Invalid option!!")
            printer()
    def newid():
        print("Welcome to new id")
        idyangugreet()


IdYangu.idyangugreet()