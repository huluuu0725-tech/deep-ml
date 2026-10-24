def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	rows=len(matrix)
	cols=len(matrix[0])
	means=[]
	if mode=='column':
		for i in range(cols):
			sum=0
			for j in range(rows):
				sum +=matrix[j][i]
			means.append(sum/rows)
	else:
		for i in range(rows):
			sum=0
			for j in range(cols):
				sum +=matrix[i][j]
			means.append(sum/cols)
	return means