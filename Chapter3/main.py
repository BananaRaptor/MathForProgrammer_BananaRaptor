from draw3d import *

from math import sqrt


# pm1 = [1, -1]
# vertices = [(x, y, z) for x in pm1 for y in pm1 for z in pm1]
#
# edges = [((-1, y, z), (1, y, z)) for y in pm1 for z in pm1] + \
#         [((x, -1, z), (x, 1, z)) for x in pm1 for z in pm1] + \
#         [((x, y, -1), (x, y, 1)) for x in pm1 for y in pm1]
# draw3d(
#     Points3D(*vertices, color=blue),
#     *[Segment3D(*edge) for edge in edges]
# )


def add(*vectors):
    return tuple(map(sum, zip(*vectors)))

# print(add((1, 1, 3), (2, 4, -4), (4, 2, -2)))

def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))


print(length((3,4,12)))



from math import sin, cos, pi


vs = [(sin(pi*t/6), cos(pi*t/6), 1.0/3) for t in range(0,24)]

running_sum = (0,0,0) #<1>
arrows = []

def scale(scalar,v):
    return tuple(scalar * coord for coord in v)

for v in vs :
    next_sum = add(running_sum, v)
    arrows.append(Arrow3D(next_sum, running_sum))
    running_sum = next_sum

print(running_sum)
draw3d(*arrows)