# 평균은 넘겠지
test_case = int(input())
for i in range(test_case):
    students = list(map(int, input().split()))
    avg = sum(students[1:])/students[0]
    cnt = 0
    for j in range(students[0]):
        if students[j+1] > avg:
            cnt += 1
    answer = cnt/students[0]*100
    print('%.3f' % answer + '%', sep='')

'''
테스트 케이스를 입력 받고
입력 받은만큼 for문을 도는데
학생 변수에 리스트로 쪼개서 넣어 주고
평균은 두번째 값부터 마지막 값까지 더한 후 첫번째 값으로 나눈 값이고
평균을 넘은 학생을 세려고 cnt 변수 설정
학생 수만큼 for문 돌면서
첫번째 값은 학생 수니까 j+1 하고 평균을 넘으면 cnt에 1을 더한다
답은 평균 넘은 학생의 비율이니까 cnt에서 학생수를 나누고 퍼센트 계산위해 100을 곱한다
(소수점 세자리까지 나오려고 좀 고생함)
round는 나누어 떨어졌을 때 세번째 자리 까지 안 나와서 f(format)을 사용 했다
%로 값을 받는걸 선언
'''