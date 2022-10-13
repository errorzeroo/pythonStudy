# 나이순 정렬
test_case = int(input())
age_list = []
for i in range(test_case):
    age, name = map(str, input().split())
    age_list.append([int(age), name])
age_list = sorted(age_list, key=lambda x: x[0])
for i in range(len(age_list)):
    print(age_list[i][0], age_list[i][1])

'''
test_case 입력 받고
빈 배열 선언한 뒤
test_case만큼 for문 돌면서
age와 name을 입력 받고 (map()은 사용 안해도 된다)
빈 age_list에 채워 준다 (중요! age를 int로 넣어야 나이순 정렬이 됨)
age_list 길이만큼 for문 돌면서
i의 첫번째, 두번째 값을 출력 한다.(i를 출력 하면 [첫번째 두번째]형태로 나옴)
'''