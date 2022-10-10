test = int(input())
for i in range(test):
	person = int(input())
	score = []
	score.append(input().split())
	score = score[0]
	int_score = []
	for j in score:
		int_score.append(int(j))
	avg = sum(int_score)/person
	hap = 0
	for k in int_score:
		if k >= avg:
			hap += 1
	print(hap, "/", person, sep='')