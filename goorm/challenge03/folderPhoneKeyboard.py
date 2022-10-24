import sys
input = sys.stdin.readline

n = int(input())
dic = {
    1 : "1.,?!",
    2 : "2ABC",
    3 : "3DEF",
    4 : "4GHI",
    5 : "5JKL",
    6 : "6MNO",
    7 : "7PQRS",
    8 : "8TUV",
    9 : "9WXYZ",
}
command = input()
ans = ''
cnt = 0
for i in range(n):
    if i == n:
        break
    else:
        if command[i+1] == command[i]:
            cnt += 1
            continue
        else:
            cnt %= len(dic[int(command[i])])
            ans += dic[int(command[i])][cnt]
            cnt = 0
print(ans)

'''
nums = int(input())
dial = input()
dialog = {'11':".", '111':',', '1111':'?', '11111':'!',
          '22':'A', '222':'B', '2222':'C', '33':'D', '333':'E', '3333':'F',
          '44':'G', '444':'H', '4444':'I', '55':'J', '555':'K', '5555':'L',
          '66':'M', '666':'N', '6666':'O', '88':'T', '888':'U', '8888':'V',
          '77':'P', '777':'Q', '7777':'R', '77777':'S',
          '99':'W', '999':'X', '9999':'Y', '99999':'Z'}
i = 0
for d in range(len(dial)):
    if dial[i] != dial[d]:
        print(dialog[dial[i:d]], end='')
        i = d
    elif dial[d] == dial[-1]:
        print(dialog[dial[i:]], end='')
        break
풀다가 틀린 내 코드
'''