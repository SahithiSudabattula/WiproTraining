from mypack.basicsahapes import areaofsquare, perimeterofsquare, areaofrect
from mypack.cricle import areaofcircle, perimeterofcircle

radius = int(input('Enter Radius:'))

print('Area:  ',areaofcircle(rad=radius))
print('Peri: ', perimeterofcircle(rad=radius))

si = int(input('enter side of sq:'))
print("area:",areaofsquare(side=si))
print("peri:",perimeterofsquare(side=si))

l = int(input('enter length:'))
b = int(input('enter breadth: '))
print('area:',areaofrect(l,b))


