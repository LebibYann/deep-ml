def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None: 
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    if det == 0:
        return None

    pr = 1/det

    return [[pr * matrix[1][1], pr * -matrix[0][1]], [pr * -matrix[1][0], pr * matrix[0][0]]]