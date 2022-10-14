# !급비 급일
password = []
while 1:
    word = input()
    if word == "END":
        break
    else:
        password.append(word)

for words in range(len(password)):
    for i in range(len(password[words])-1, -1, -1):
        print(password[words][i], end='')
    print('')

'''
빈 배열 만들고
무한 루프문 돌면서
문장을 입력 받는다
END가 입력 되면 무한 루프 탈출 
입력 받은 문장을 password에 넣는다
password 길이만큼 for문 돌면서
이중으로 password[i]길이를 돌며
마지막 문자부터 첫문자까지 출력 한다.
password[i] for문이 끝나면 줄바꿈 한다.  
'''