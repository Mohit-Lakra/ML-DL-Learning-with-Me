# The Gram-Schmidt process
This is the algorithm used to take a "messy" basis and turn it into a "perfect" orthonormal basis.

## The Logic
Suppose you have two vectors $\mathbf{x}_1$ and $\mathbf{x}_2$ that aren't perpendicular. To make them orthogonal:
1. Keep $\mathbf{x}_1$ as your first direction. Let $\mathbf{v}_1 = \mathbf{x}_1$.
2. For $\mathbf{x}_2$, subtract the part of it that points in the direction of $\mathbf{v}_1$. What's left is the "perpendicular" part.

## The Formulas (for $k$ vectors)
1. $\mathbf{v}_1 = \mathbf{x}_1$
2. $\mathbf{v}_2 = \mathbf{x}_2 - \text{proj}_{\mathbf{v}_1} \mathbf{x}_2$
3. $\mathbf{v}_3 = \mathbf{x}_3 - \text{proj}_{\mathbf{v}_1} \mathbf{x}_3 - \text{proj}_{\mathbf{v}_2} \mathbf{x}_3$

After you get all the $\mathbf{v}$ vectors (which are now orthogonal), you divide each by its own length to make them orthonormal.
