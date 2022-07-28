test_case = int(input())
for i in range(test_case):
    calendar = input()
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if int(calendar[4:6]) >= 1 and int(calendar[4:6]) <= 12:
        if int(calendar[6:]) >= 1 and int(calendar[6:]) <= days[int(calendar[4:6])-1]:
            print('#', i+1, ' ', calendar[:4], '/', calendar[4:6], '/', calendar[6:], sep='')
        else:
            print('#', i+1, ' ', -1, sep='')
    else:
        print('#', i+1, ' ', -1, sep='')

'''
테스트 케이스 인풋 받고
테스트 케이스만큼 반복문 돌린다.
날짜를 문자열로 인풋 받고
월별 일자를 배열에 저장한다. (if문을 여러개 쓰지 않기 위해)
월이 1-12까지 수인지 if문으로 판단. 아니면 -1 출력
일이 월에 따라 맞는 일 수인지 판단. 아니면 -1 출력 맞으면 년/월/일 출력  
'''