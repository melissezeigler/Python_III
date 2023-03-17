#Calc Circumference
from math import pi

def calcCircumference():
    radius = float(input("What is the circle's radius? "))
    circumference = radius * pi **2
    return(f'The circumference of your circle is {circumference}')

def houseArea():
    area = float(input('What is the Length of the house? ')) * float(input('What is the width of the house? '))
    return(f'The area of the house is {area}')

