# 검증수
koi = map(int, input().split())
num = []
for i in koi:
    num.append(i ** 2)  # 빈 리스트에 koi의 각 값 제곱 추가
print(sum(num) % 10)  # 10으로 나눈 나머지 출력