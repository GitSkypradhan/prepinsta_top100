import math
# volume of sphere = 4/3 *pi*radius**3


# def sphere_volume(radius):
#     volume = round(4/3*math.pi*radius**3, 2)
#     print(volume)

sphere_volume = lambda radius: print(round(4/3*math.pi*radius**3,2))


sphere_volume(4)