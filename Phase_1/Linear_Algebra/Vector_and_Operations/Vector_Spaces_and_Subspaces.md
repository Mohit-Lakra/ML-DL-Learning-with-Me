# Vector Spaces and Subspaces

Vector is not just an arrow or list of numbers. It is a mathematical object that can be added together and multiplied by scalars.

## Vector Spaces

A vector space is a  collection of vectors that can be added together and multiplied by scalars and still remains the same collection. For example, the set of all 2D vectors is a vector space. The set of all 3D vectors is also a vector space.

Rules :- 
1. u + v in V for all u, v in V
2. u + v = v + u for all u, v in V
3. (u + v) + w = u + (v + w) for all u, v, w in V
4. There exists a zero vector 0 in V such that u + 0 = u for all u in V
5. For every u in V, there exists a vector -u in V such that u + (-u) = 0
6. c * u in V for all c in R and u in V
7. c * (u + v) = c * u + c * v for all c in R and u, v in V
8. (c + d) * u = c * u + d * u for all c, d in R and u in V
9. c * (d * u) = (c * d) * u for all c, d in R and u in V
10. 1 * u = u for all u in V

## Vector Subspaces

A vector subspace is a subset of a vector space that is also a vector space. For example, the set of all 2D vectors that lie on a line through the origin is a vector subspace of the set of all 2D vectors.

Rules :-
1. The zero vector is in the subspace.
2. If u and v are in the subspace, then u + v is in the subspace.
3. If u is in the subspace and c is a scalar, then c * u is in the subspace.

## Four Fundamental Subspaces of a Matrix

1. Column Space: The set of all linear combinations of the columns of a matrix. This tells us if Ax = b has a solution for a given b.
2. Null Space: The set of all solutions to the homogeneous equation Ax = 0. This measures the redundancy in the system.
3. Row Space: The set of all linear combinations of the rows of a matrix. This is the column space of the transpose of the matrix.
4. Left Null Space: The set of all solutions to the homogeneous equation A^T y = 0. This is the null space of the transpose of the matrix.


