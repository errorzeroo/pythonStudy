n = int(input())
sub = list(map(int, input().split()))
score = []
for i in sub:
    score.append((i / max(sub)) * 100)
print(sum(score)/n)