# 팰린드롬수
while 1:                  # 무한 루프
    pelindlom = input()
    if pelindlom == '0':  # '0'이 들어 오면 종료
        break
    elif pelindlom == pelindlom[::-1]:
        print('yes')      # 앞으로 읽어도 뒤로 읽어도 같으면 팰린드롬
    else:
        print('no')