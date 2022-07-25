num = int(input())
score = list(map(int, input().split()))
mid = num // 2
score.sort()
print(score[mid])