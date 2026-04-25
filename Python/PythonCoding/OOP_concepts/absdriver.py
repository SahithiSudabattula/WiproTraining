from OOP_concepts.rectangle import Rectangle
from OOP_concepts.square import Square

sqrobj = Square(10)

print(f'Area: {sqrobj.calculate_area()} \t Perimeter: {sqrobj.calculate_perimeter()}')

rectobj = Rectangle(10, 5)
print(f'Area: {rectobj.calculate_area()} \t Perimeter: {rectobj.calculate_perimeter()}')



