def shoelace_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0

    sum1 = 0.0
    sum2 = 0.0

    for i in range(n - 1):
        x_i, y_i = vertices[i]
        x_j, y_j = vertices[i + 1]
        sum1 += x_i * y_j
        sum2 += y_i * x_j

    x_last, y_last = vertices[-1]
    x_first, y_first = vertices[0]
    sum1 += x_last * y_first
    sum2 += y_last * x_first

    return abs(0.5 * (sum1 - sum2))


# Example Usage:
if __name__ == "__main__":
    # Triangle vertices
    vertices_anticlockwise = [(0, 0), (3, 6), (6, 0)]
    area = shoelace_area(vertices_anticlockwise)
    print(f"Area (Triangle): {area}")

    # square
    vertices_clockwise = [(0, 0), (0, 4), (4, 4), (4, 0)]
    area = shoelace_area(vertices_clockwise)
    print(f"Area (Square): {area}")