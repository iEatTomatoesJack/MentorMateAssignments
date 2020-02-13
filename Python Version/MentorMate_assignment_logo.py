"""This is the solution for the MentorMate assignment using python"""
from MentorMateClass import DoubleMLetter #Importing class from another file to be more clean the code




widthInput = int(input("Write the width of the double M: "))
doubleM = DoubleMLetter() 
doubleM.print_logo(widthInput) 
print("\n")
doubleM.alternative_print_logo(widthInput) 
