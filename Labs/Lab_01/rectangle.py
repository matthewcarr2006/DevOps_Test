
"""
User inputs width and length.
Perimeter and area are calculated based on the input. 
"""

length = int(input("Enter length: "))
width = int(input("Enter width: "))

perimeter = 2 * (length + width)
area = length * width
print(f"Perimeter: {perimeter}")
print(f"Area: {area}")