﻿class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width
        
    def area(self): # Class function
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width           # Construstor
        
    
    
length = int(input("Enter Length:"))
width = int(input("Enter width:"))
r = Rectangle(length, width)
print("Area:", r.area())
print("Perimeter:", r.perimeter())

input()