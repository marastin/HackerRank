from collections import namedtuple

# Example 1
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) + ( pt1.y * pt2.y )
print(dot_product)

# Example 2
Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print(xyz)
print(xyz.Class)




from collections import namedtuple
N = int(input())
title = input().split()
Student = namedtuple('Student', title)
s = []
for _ in range(N):
    values = input().split()
    s.append(int(Student(*values).MARKS))

print(sum(s)/N)