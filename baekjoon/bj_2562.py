# 최댓값
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
    num.append(int(input()))  # 인풋 받을 숫자를 빈 리스트에 추가
m = max(num)  # 최댓값 추출
index = num.index(m)  # 최댓값의 인덱스 추출
print(m, index+1, sep='\n')
