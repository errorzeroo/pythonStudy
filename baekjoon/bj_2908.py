num_a, num_b = input().split()
if num_a[::-1] > num_b[::-1]:
    print(num_a[::-1], sep=',')
else:
    print(num_b[::-1])