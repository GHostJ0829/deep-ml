def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "column":
		for col in zip(*matrix):
			means.append(sum(col)/len(col))
	if mode == "row":
		for row in matrix:
			means.append(sum(row)/len(row))
	return means