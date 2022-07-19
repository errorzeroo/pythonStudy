while 1:
    pelindlom = input()
    if pelindlom == '0':
        break
    elif pelindlom == pelindlom[::-1]:
        print('yes')
    else:
        print('no')