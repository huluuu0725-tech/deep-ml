def OSA(source: str, target: str) -> int:
	# Your code here
	m=len(source)
	n=len(target)
	bp=[[0]*(n+1) for i in range(m+1)]
	for i in range(1,m+1):
		bp[i][0]=i
	for j in range(1,n+1):
		bp[0][j]=j	
	for i in range(1,m+1):
		for j in range(1,n+1):
			cost=0 if source[i-1]==target[j-1] else 1
			bp[i][j]=min(
				bp[i-1][j]+1,#删除
				bp[i][j-1]+1,#增加
				bp[i-1][j-1]+cost#替换
			)
			if i>=2 and j>=2 and source[i-2]==target[j-1] and source[i-1]==target[j-2]:
				bp[i][j]=min(
					bp[i][j],
					bp[i-2][j-2]+1
				)
	return bp[m][n]
