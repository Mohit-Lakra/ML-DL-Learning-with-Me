def add_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
        
    result = [vector1[i] + vector2[i] for i in range(len(vector1))]
    return result

def scale_vector(scalar, vector):
    result = [scalar * vector[i] for i in range(len(vector))]
    return result

def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
        
    result = sum(vector1[i] * vector2[i] for i in range(len(vector1)))
    return result

# Example usage:
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
print("Addition:", add_vectors(vector1, vector2))
print("Scaling:", scale_vector(2, vector1))
print("Dot Product:", dot_product(vector1, vector2))
