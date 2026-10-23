def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	iscolumn = mode == "column"
	
	xaxis= len(matrix[0]) if iscolumn else len(matrix)
	yaxis= len(matrix) if iscolumn else len(matrix[0])
	means: list[float] = [0] * xaxis

	for i in range(xaxis):
		for j in range(yaxis):
			means[i] += matrix[j][i] if iscolumn else matrix[i][j]
		means[i] /= yaxis

	return means