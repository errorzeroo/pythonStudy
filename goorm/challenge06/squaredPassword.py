num = int(input())
password = input()
word = ''
for i in range(1, num+1, 2):
    if int(password[i]) < 6:
        if ord(password[i-1]) + int(password[i])**2 > 122:
            word += chr(ord(password[i - 1]) + int(password[i]) ** 2 - 26)
        else:
            word += chr(ord(password[i-1]) + int(password[i]) ** 2)
    elif int(password[i]) == 6 or int(password[i]) == 7:
        if ord(password[i-1]) + int(password[i])**2 - 26 > 122:
            word += chr(ord(password[i - 1]) + int(password[i]) ** 2 - 52)
        else:
            word += chr(ord(password[i-1]) + int(password[i]) ** 2 - 26)
    elif int(password[i]) == 8:
        if ord(password[i-1]) + 12 > 122:
            word += chr(ord(password[i - 1]) - 14)
        else:
            word += chr(ord(password[i-1]) + 12)
    else:
        if ord(password[i-1]) + 3 > 122:
            word += chr(ord(password[i - 1]) - 23)
        else:
            word += chr(ord(password[i-1]) + 3)
print(word)