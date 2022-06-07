koi = map(int, input().split())
num = []
for i in koi:
    num.append(i ** 2)
print(sum(num) % 10)