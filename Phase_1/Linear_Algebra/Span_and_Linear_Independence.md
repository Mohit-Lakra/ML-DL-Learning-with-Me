# Span and Linear Independence

## Span
The Span of a set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k\}$ is the set of all possible linear combinations of those vectors.

### Mathematical Definition
A vector $\mathbf{b}$ is in the span if you can find scalars $c_1, c_2, \dots, c_k$ such that:
$$\mathbf{b} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_k\mathbf{v}_k$$

### Geometric Intuition
- One Vector :
The span is a line passing through the origin (unless it's the zero vector).
- Two Vectors : The span is a plane passing through the origin
- Three vectors : The span is the entire 3D space ($\mathbb{R}^3$).

## Linear Independence
Linear independence tells us if every vector in a set can be expressed as a linear combination of the others.

### The Formal Test
A set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n\}$ is linearly independent if the only solution to the equation:
$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_n\mathbf{v}_n = \mathbf{0}$$
is the trivial solution: $c_1 = c_2 = \dots = c_n = 0$.

If there is any other way to reach the zero vector (meaning at least one $c_i \neq 0$), the vectors are linearly dependent.

- Dependent: At least one vector can be written as a combination of the others. It is redundant.
- Independent: No vector can be written as a combination of the others. Each vector adds new information.

