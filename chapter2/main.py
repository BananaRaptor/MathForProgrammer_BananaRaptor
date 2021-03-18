from functools import reduce

from numpy.ma import arctan

from vector_drawing import *

from math import tan, pi, sin, cos, asin, acos, atan2

from random import uniform

dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0),
                (-2, 1), (-1, 0), (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)]


def add(*vectors):
    return sum([vector[0] for vector in vectors]), sum([v[1] for v in vectors])


def subtract(v1, v2):
    return v1[0] - v2[0], v1[1] - v2[1]


def length(vector):
    return sqrt(vector[0] ** 2 + vector[1] ** 2)


def scale(scalar, vector):
    return vector[0] * scalar, vector[1] * scalar


def translate(translation, vectors):
    return [add(vector, translation) for vector in vectors]


def distance(vector1, vector2):
    return length(subtract(vector1, vector2))


def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i + 1) % len(vectors)]) for i in range(0, len(vectors))]
    return sum(distances)


# print(length(scale(pi,(sqrt(2),sqrt(3)))))
# print(length((sqrt(2),sqrt(3))) * pi)
# dino_vectors2 = [add((-1.5, -2.5), v) for v in dino_vectors]

# draw(
#     Points((2, 2), (-1, 3)),
#     Segment((2, 2), (-1, 3), color=red)
# )


# print(max(dino_vectors, key=length))


# def printTheHundredDinos(dino):
#     translations = [(12*x,10*y)
#                     for x in range(-5,5)
#                     for y in range(-5,5)]
#     dinos = [Polygon(*translate(t, dino),color=blue)
#              for t in translations]
#     draw(*dinos, grid=None, axes=None, origin=None)

# printTheHundredDinos(dino_vectors)


# u = (-1, 1)
# v = (1, 1)
#
#
# def random_r():
#     return uniform(-3, 3)
#
#
# def random_s():
#     return uniform(-1, 1)
#
#
# possibilities = [add(scale(random_r(), u), scale(random_s(), v))
#                  for i in range(0, 500)]
#
# draw(
#     Points(*possibilities)
# )

# print(perimeter(dino_vectors))

# for n in range(-12, 15):
#     for m in range(-14, 13):
#         if distance( (n, m), (1, -1)) == 13 and n > m > 0:
#             print((n, m))


polar_coords = [(cos(5 * x * pi / 500.0), 2 * pi * x / 1000.0) for x in range(0, 1000)]


def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length * cos(angle), length * sin(angle))


def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return (length(vector), angle)


# vectors = [to_cartesian(p) for p in polar_coords]
#
# draw(
#      Polygon(*vectors, color=blue)
#  )


def rotate(rotation, vectors):
    vectors_polar = [to_polar(v) for v in vectors]
    vectors_rotated_polar = [(length, angle + rotation) for length, angle in vectors_polar]
    return [to_cartesian(vector) for vector in vectors_rotated_polar]


def regular_polygon(n):
    return [to_cartesian((1, (2 * pi / n) * i)) for i in range(0, n)]

print(regular_polygon(7))

new_dino = translate((8, 8), rotate(5 * pi / 3, dino_vectors))

draw(
    Polygon(*regular_polygon(7))
)
