def zero_matrix(m):
	n = len(m)
	zero_x = []
	zero_y = []
	for i in range(n):
		for j in range(n):
			if m[i][j] == 0:
				zero_x.append(i)
				zero_y.append(j)

	for i in zero_x:
		for j in range(n):
			m[i][j] = 0

	for j in zero_y:
		for i in range(n):
			m[i][j] = 0

	return m

print(zero_matrix([
			[1, 0, 3, 0, 5],
			[6, 7, 8, 9, 10],
			[11, 12, 13, 14, 15],
			[16, 17, 18, 19, 20],
			[21, 22, 23, 24, 25]
		]))