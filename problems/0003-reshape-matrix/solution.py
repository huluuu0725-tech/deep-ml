import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if len(new_shape)!=2 or any(i<=0 for i in new_shape):
		return []
	try:
		matrix=np.array(a)
		if matrix.ndim !=2:
			return []
		return matrix.reshape(new_shape).tolist()
	except ValueError:
		return []