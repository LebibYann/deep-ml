def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    nmatrix : list[list[int|float]] = []

    for i in range(len(a[0])):
        nmatrix.append([])
        for j in range(len(a)):
            nmatrix[i].append(a[j][i])
    return nmatrix