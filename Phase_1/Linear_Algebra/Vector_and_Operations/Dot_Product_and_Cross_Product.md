# Dot Product and Cross Product

## Dot Product
The dot product (also known as the scalar product) take two vectors and return a single number. It tells about the measure of alignment.

u = [u1, u2, u3]
v = [v1, v2, v3]

Algebraic definition:
The dot product is calculated as:
u . v = u1 * v1 + u2 * v2 + u3 * v3

Geometric interpretation:
The dot product can be expressed as:
u . v = ||u|| * ||v|| * cos(theta)

Where ||u|| and ||v|| are the magnitudes of the vectors, and theta is the angle between them.

1) If the dot product is positive, it means the vectors are pointing in the same general direction (acute angle).
2) If the dot product is negative, it means the vectors are pointing in opposite directions (obtuse angle).
3) If the dot product is zero, it means the vectors are perpendicular (orthogonal) to each other.

## Cross Product
The cross product (also known as the vector product) takes two vectors in three-dimensional space and returns a new vector that is perpendicular to both of the original vectors. The magnitude of the cross product is equal to the area of the parallelogram formed by the two vectors.

u = [u1, u2, u3]
v = [v1, v2, v3]

Algebraic definition:

The cross product is calculated as:

u x v = det| i   j   k  |
           | u1  u2  u3 |
           | v1  v2  v3 |

Where i, j, and k are the unit vectors in the x, y, and z directions, respectively.


Geometric interpretation:
The resulting vector has 2 important properties:
1) It is perpendicular to both u and v. Direction can be determined using the right-hand rule.
2) The magnitude of the cross product is given by:
||u x v|| = ||u|| * ||v|| * sin(theta)

Where ||u|| and ||v|| are the magnitudes of the vectors, and theta is the angle between them.
