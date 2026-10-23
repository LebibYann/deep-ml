def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	m = len(b)
	dot: list[list[int|float]] = [0] * len(a)

	for row in a:
		if len(row) != m:
			return -1

	for i in range(len(a)):
		for j in range(m):
			dot[i] += a[i][j] * b[j] 
	return dot