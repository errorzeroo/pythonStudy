def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx, num in enumerate(phone_book):
        if num == phone_book[-1]:
            break
        else:
            if num == phone_book[idx+1][:len(num)]:
                answer = False
                break

    return answer

'''
phone_book을 정렬한다음
인덱스와 값을 가져와서
마지막 값은 다음값과 비교 할 수 없어서 문을 빠져나오고
값(num)과 다음값에서 값만큼만 잘라서 비교할 때
같으면 answer을 false로
'''