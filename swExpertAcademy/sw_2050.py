alpha = input().upper()
for i in range(len(alpha)):
    if ord(alpha[i]) >= 65 and ord(alpha[i]) <= 90:
        print(ord(alpha[i]) - 64, end=' ')
    else:
        continue
