star = int(input())  # 별 출력할 숫자 input 받기
for i in range(1, star+1):  # input받을 숫자를 반복
    for j in range(i):  # i를 반복
        print('*', end='')  # *을 i만큼 반복 만큼 출력
    print()  # \n해줌