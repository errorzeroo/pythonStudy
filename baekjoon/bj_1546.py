n = int(input())
sub = list(map(int, input().split()))
score = []
for i in sub:  # input 받은 숫자를 만큼 반복 들어 간다
    score.append((i / max(sub)) * 100)  # score에 i를 최대수로 나눈 수를 곱해서 평균 구한걸 추가
print(sum(score)/n)