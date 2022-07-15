while True:  # while 안에서 예외 처리 해서 인풋 받지 않으면 빠져 나간다
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
