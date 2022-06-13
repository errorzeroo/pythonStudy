a, b = map(int, input().split())  # 두 수를 띄어 쓰기를 통해 받는다.

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')