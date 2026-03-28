# Norms (L1, L2, Lp)

Mathematically, a norm is a function f(x) that maps a vector to real scalar and must satisfies the following properties:
1. Non-negativity: f(x) >= 0
2. Definiteness: f(x) = 0 if and only if x = 0
3. Homogeneity: f(ax) = |a| * f(x) for any scalar
4. Triangle inequality: f(x + y) <= f(x) + f(y)

## General Lp Norm
The general Lp norm of a vector x in Rn is defined as:
$` \|x\|_p = \left( \sum_{i=1}^{n} |x_i|^p \right)^{\frac{1}{p}} `$

## The Big Three Norms

1. L1 Norm (Manhattan Norm):
$` \|x\|_1 = \sum_{i=1}^{n} |x_i| `$
Calculated by summing the absolute values of the components.

Visual: Imagine walking in a grid-based city (like Manhattan). You can't go diagonally; you must go "over and up."

2. L2 Norm (Euclidean Norm):
$` \|x\|_2 = \sqrt{\sum_{i=1}^{n} x_i^2} `$
Calculated by taking the square root of the sum of the squares of the components.
Visual : Shortest distance from any 2 points in a 2D plane.

3. $L_\infty$ Norm:

$$\|\mathbf{x}\|_\infty = \max(|x_1|, |x_2|, \dots, |x_n|)$$
As $p$ approaches infinity, the largest absolute element dominates the sum
Visual: It only cares about the single largest coordinate

## Shape of Norms
1. L1 is diamond shaped. The corners of the diamond lie on the axes.
2. L2 is circular.
3. $L_\infty$ is a square.



