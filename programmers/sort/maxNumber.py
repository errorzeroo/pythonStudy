def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))  # [str(i) for i in numbers]
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    for i in range(len(numbers)): answer += numbers[i]
    return str(int(answer))

'''
print(solution([0, 0, 0, 0]))
정답 문자열 초기화
numbers의 모든 값을 str로 변환 해준다.
numbers의 값을 정렬 해주는데, 가장 큰 수를 구해야 하므로 모든 값에 3을 곱해준 값을 내림차순으로 정렬 한다.
3을 곱하는 이유는 수의 범위가 1000까지 이고, 30, 3이 있을 때 330이 303보다 크기 때문이다.
for문을 사용 하여 answer에 값을 저장 한다.
join을 사용 하는 방법 : return str(int(''.join(numbers)))
0000이 나올 수도 있으니 리턴할 때 int로 바꿨다가 str로 바꿔 준다.
'''