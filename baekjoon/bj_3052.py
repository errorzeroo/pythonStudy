list_num = []  # 빈 list 생성

for i in range(10):  # 0부터 9까지 for문
    num = int(input())  # 새로운 변수 input 받기
    if (num % 42) not in list_num:  # 42로 나눴을 때 나머지가 list_num에 없을 때 추가
        list_num.append(num % 42)

print(len(list_num))  # list_num의 길이를 출력