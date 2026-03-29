def is_in_span(vectors, target):
    num_rows = len(target)
    num_cols = len(vectors)

    matrix = [[vectors[j][i] for j in range(num_cols)] for i in range(num_rows)]
    for i in range(num_rows):
        matrix[i].append(target[i])

    pivot_row = 0
    for j in range(num_cols):
        if pivot_row >= num_rows:
            break

        max_val = abs(matrix[pivot_row][j])
        max_row = pivot_row
        for r in range(pivot_row + 1, num_rows):
            if abs(matrix[r][j]) > max_val:
                max_val = abs(matrix[r][j])
                max_row = r

        matrix[pivot_row], matrix[max_row] = matrix[max_row], matrix[pivot_row]

        if abs(matrix[pivot_row][j]) < 1e-10:
            continue

        for r in range(num_rows):
            if r != pivot_row:
                factor = matrix[r][j] / matrix[pivot_row][j]
                for c in range(j, num_cols + 1):
                    matrix[r][c] -= factor * matrix[pivot_row][c]

        pivot_row += 1

    for r in range(num_rows):
        all_zeros = all(abs(matrix[r][c]) < 1e-10 for c in range(num_cols))
        target_val_exists = abs(matrix[r][-1]) > 1e-10
        if all_zeros and target_val_exists:
            return False
    return True

# --- Test Cases ---
# Case 1: Standard basis. Should be True.
print(f"Case 1: {is_in_span([[1, 0], [0, 1]], [3, 3])}") 

# Case 2: Linearly dependent vectors, but target is reachable. Should be True.
# [3, 3] = 3*[1, 1] + 0*[2, 2]
print(f"Case 2: {is_in_span([[1, 1], [2, 2]], [3, 3])}") 

# Case 3: Linearly dependent vectors, target NOT reachable. Should be False.
print(f"Case 3: {is_in_span([[1, 1], [2, 2]], [1, 0])}")

