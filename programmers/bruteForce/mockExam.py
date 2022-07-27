def solution(answers):
    math_x = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    max_math = []
    count_math = [0, 0, 0]
    for i, val in enumerate(answers):
        for idx, j in enumerate(math_x):
            if val == j[i % len(j)]:
                count_math[idx] += 1
    for idx, cnt in enumerate(count_math):
        if max(count_math) == cnt:
            max_math.append(idx+1)
    print(count_math)
    return max_math

'''
완전탐색 - 부르트포스 알고리즘
수포자들의 패턴 리스트를 하나로 담는다(따로 담아도 됨) = math_x
max_math = 가장 많이 맞춘 수포자의 리스트
count_math = 수포자123의 맞춘 개수

enumerate는 인덱스와 값을 가져오는 함수
첫번째 for에서 답의 인덱스 i와 값 val을 가져온다
이중 for에서 수포자의 인덱스 idx와 리스트 j를 가져온다
답answers의 값 val이 -j의 길이를 나눈 나머지 값-
(답이 j의 길이 보다 큰경우 j를 반복 하기위해)의 인덱스의 값이랑 같으면
count_math에 math_x의 인덱스 자리에 1을 더한다

count_math을 도는데 가장 큰 값이 cnt랑 같을 때
인덱스 idx보다 하다 큰 수를 max_math에 저장
'''