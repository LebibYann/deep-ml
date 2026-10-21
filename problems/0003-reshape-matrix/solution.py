import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	previous_shape = (len(a), len(a[0]))
	if previous_shape[0] * previous_shape[1] != new_shape[0] * new_shape[1]:
		return [] 
	
	reshaped_matrix: list[list[int|float]] = [];
	for i in range(new_shape[0]):
		reshaped_matrix.append([])
		for j in range(new_shape[1]):
			x = int((i * new_shape[1] + j) / previous_shape[1])
			y = (i * new_shape[1] + j) % previous_shape[1]
			reshaped_matrix[i].append(a[x][y])

	return reshaped_matrix