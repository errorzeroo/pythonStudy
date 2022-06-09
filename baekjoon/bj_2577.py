A = int(input())
B = int(input())
C = int(input())
mul = list(str(A*B*C))
for i in range(10):
    i = mul.count(str(i))
    print(i)