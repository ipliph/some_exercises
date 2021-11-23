class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):    # return string "Vector(x, y, z)"
        return('Vector({},{},{})'.format(self.x,self.y,self.z))
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False    # v == w

    def __ne__(self, other):        # v != w
        if self.x != other.x or self.y != other.y or self.z != other.z:
            return True
        else:
            return False

    def __add__(self, other):  # v + w

        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)


    def __sub__(self, other):    # v - w

        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)

    def __mul__(self, other):
        return  self.x*other.x + self.y*other.y + self.z*other.z # return the dot product (number)

    def cross(self, other):
        #the cross product
        #a x b = (a2 * b3 - a3 * b2,       a3 * b1 - a1 * b3,        a1 * b2 - a2 * b1)

        return Vector((self.y*other.z) - (self.z*other.y),   (self.z*other.x) - (self.x*other.z) ,     (self.x*other.y) - (self.y*other.x))  
        # return the cross product (Vector)

    def length(self):    # the length of the vector
        import math
        return math.sqrt((self.x**2) + (self.y**2) + (self.z**2))

    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended


vector_1 = Vector(1,2,3)
vector_2 = Vector(4,5,6)
import math
assert vector_1 != vector_2 
assert vector_1 + vector_2 == Vector(5,7,9)
assert vector_1 - vector_2 == Vector(-3,-3,-3)
assert vector_1 * vector_2 == 32
assert vector_1.cross(vector_2) == Vector(-3,6,-3)
assert vector_1.length() == math.sqrt(14)
S = set([vector_1, vector_1, vector_2])
assert len(S) == 2


print('')

#Create a function find_axis(v1, v2) which returns the unit vector v3, 
#where v3 is perpendicular to the vectors v1 and v2. 
#If the vectors v1 and v2 are parallel (or zero) then the function should raise an exception (ValueError) 
#[Hint: v1 and v2 are parallel if the cross product v1 x v2 is zero]. 
#Vectors are instances of the Vector class from Homework 6. 


def find_axis(v1,v2):
    vector_3 = v1.cross(v2)
    
    if vector_3 == Vector(0,0,0):
        raise ValueError("parallel vectors")

    print(vector_3 , 'is perpendicular to the vectors' , v1 ,'and' , v2)


find_axis(Vector(1,1,1),Vector(2,3,2))

#Create the following infinite iterators:
#(a) returning 0, 1, 0, 1, 0, 1, ...,
#(b) returning random sequence with 0 and 1,
#(c) returning 0, 1, 0, -1, 0, 1, 0, -1, ... 

import itertools
import random

it1 = itertools.cycle([0,1])
L_it1 = []
for x in range(10):
    L_it1.append(next(it1))
print(L_it1)

def it2(x):
    L_it2 = []
    end = 0
    while x > end:
        num = random.randrange(2)
        in2 = itertools.repeat(num)
        L_it2.append(next(in2))
        end = end + 1
    print(L_it2)

it2(10)

it3 = itertools.cycle([0,1,0,-1])
L_it3 = []
for x in range(10):
    L_it3.append(next(it3))
print(L_it3)

