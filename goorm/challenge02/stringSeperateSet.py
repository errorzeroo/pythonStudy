num = int(input())
alpha = input()
cnt = 1
for i in range(1, len(alpha)):
    if alpha[i] != alpha[i-1]:
        cnt += 1
print(cnt)