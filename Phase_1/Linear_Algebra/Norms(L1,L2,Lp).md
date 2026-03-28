# Norms (L1, L2, Lp)

Mathematically, a norm is a function f(x) that maps a vector to real scalar and must satisfies the following properties:
1. Non-negativity: f(x) >= 0
2. Definiteness: f(x) = 0 if and only if x = 0
3. Homogeneity: f(ax) = |a| * f(x) for any scalar
4. Triangle inequality: f(x + y) <= f(x) + f(y)

## General Lp Norm
The general Lp norm of a vector x is defined as:
$` \|x\|_p = \left( \sum_{i=1}^{n} |x_i|^p \right)^{\frac{1}{p}} `$
where p is a positive real number. The Lp norm is a generalization of the L1 and L2 norms, and it can be used to measure the length of a vector in different ways depending on the value of p.
