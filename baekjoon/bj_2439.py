star = int(input())  # 별 출력할 숫자 input 받기
for i in range(1, star+1):  # input 받을 숫자를 반복
    for j in range(star-i):  # i의 반대 만큼 반복
        print(' ', end='')  # 띄어 쓰기를 i의 반대 만큼 출력
    for j in range(i):  # i를 반복
        print('*', end='')  # *을 i만큼 반복 만큼 출력
    print()  # \n해줌