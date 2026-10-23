def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    m, n, k = len(a), len(b[0]), len(b)
    matrix: list[list[int|float]] = []

    if (k != len(a[0])):
        return -1

    for x in range(m):
        matrix.append([])
        for y in range(n):
            matrix[x].append(0)
            for z in range(k):
                matrix[x][y] += a[x][z] * b[z][y]
    return matrix