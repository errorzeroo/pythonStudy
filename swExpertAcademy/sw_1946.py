test_case = int(input())              # 테스트 케이스 인풋
for i in range(test_case):            # 테스트 케이스만큼 for문
    alpha_num = int(input())          # 알파벳 개수 인풋
    letter = ''                       # 저장할 글씨 초기화
    for j in range(alpha_num):        # 알파벳 개수만큼 for문
        alpha, num = input().split()  # 알파벳과 개수 인풋
        letter += alpha*int(num)      # 알파벳을 개수만큼 곱해서 저장
    print(f"#{i+1}")                  # 테스트 케이스 출력
    for k in range(len(letter)//10+1):
        print(letter[k*10:(k+1)*10])  # 알파벳을 10단위로 쪼개기

# 알파벳 길이만큼 10으로 나눠서 출력을 할건데 나머지도 출력하기 위해 +1 해줌
# 글씨를 10단위로 슬라이싱을 할건데 초기값이 0이고 이후로 10씩 올라가서 *10을 해줌