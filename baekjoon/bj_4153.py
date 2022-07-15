while 1:
    triangle = list(map(int, input().split()))
    triangle.sort()
    Heru = triangle[2]
    Auset = triangle[1]
    Ausar = triangle[0]
    if Heru == 0 and Auset == 0 and Ausar == 0:
        break
    elif Heru**2 == Auset**2 + Ausar**2:
        print('right')
    else:
        print('wrong')