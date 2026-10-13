import math


def cosine_distance(vec1, vec2):
    if not isinstance(vec1, list) or not isinstance(vec2, list):
        print("vec1 and vec2 must be list")

    if len(vec1) == 0 or len(vec2) == 0:
        print("vec1 and vec2 must be non-empty")

    if len(vec1) != len(vec2):
        print(f"vec1 and vec2 must be same length")

    for i, (v1, v2) in enumerate(zip(vec1, vec2)):
        if not isinstance(v1, (int, float)) or not isinstance(v2, (int, float)):
            print("vec1 and vec2 must be int or float")

    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))

    norm1 = math.sqrt(sum(v ** 2 for v in vec1))
    norm2 = math.sqrt(sum(v ** 2 for v in vec2))

    if norm1 == 0:
        print("vec1 is zero a null(zero) vector (norm == 0)")

    if norm2 == 0:
        print("vec2 is zero a null(zero) vector (norm == 0)")

    cosine_similarity = dot_product / (norm1 * norm2)

    distance = 1 - cosine_similarity

    print(distance)


if __name__ == '__main__':
    cosine_distance([1, 2, 3], [4, 5, 6])
    cosine_distance([1, 0, 0], [1, 0, 0])
    # test edge cases
    cosine_distance([1, 2, 3], [4, 5])
    cosine_distance((1, 2, 3), [4, 5, 6])
    # cosine_distance([], [1, 2, 3])
    # cosine_distance([1, 2, 3], [0, 0, 0])
    # cosine_distance([0, 0, 0], [1, 2, 3])
    # cosine_distance([1, "a", 3], [4, 5, 6])
