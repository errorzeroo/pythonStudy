while True:  # a, b 둘다 0 일 때 멈추고 아니면 덧셈 출력
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)
