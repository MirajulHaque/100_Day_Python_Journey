import math

height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
coverage = 5


def point_calc(height, width, cover):
    cans = (height * width) / cover
    return cans


cans = math.ceil(point_calc(height, width, coverage))
print(f"You'll need {cans} cans of point.")
