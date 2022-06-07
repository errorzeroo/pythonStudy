# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# f = int(input())
# g = int(input())
# h = int(input())
# i = int(input())
# num = a, b, c, d, e, f, g, h, i
num = []
for i in range(9):
    num.append(int(input()))
m = max(num)
index = num.index(m)
print(m, index+1, sep='\n')
