# 상수
num_a, num_b = input().split()
if num_a[::-1] > num_b[::-1]:    # 문자열 슬라이싱 거꾸로 뽑기
    print(num_a[::-1])  # 거꾸로 큰 수 출력
else:
    print(num_b[::-1])