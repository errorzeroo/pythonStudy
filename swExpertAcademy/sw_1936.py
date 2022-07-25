A, B = map(int, input().split())
if A < B:
    print('B')
elif A == 1 and B == 3:
    print('A')
elif B == 1 and A == 3:
    print('B')
else:
    print('A')