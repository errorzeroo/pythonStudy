from collections import defaultdict
def solution(fees, records):
    answer = []
    cars = {}
    times = defaultdict(int)

    for r in records:
        time, num, status = r.split()
        if status == 'IN':
            cars[num] = time
        else:
            h1, m1 = map(int, cars[num].split(':'))
            h2, m2 = map(int, time.split(':'))
            times[num] += ((h2 - h1) * 60) + m2 - m1
            del cars[num]

    for num, time in cars.items():
        h1, m1 = map(int, cars[num].split(':'))
        times[num] += ((23 - h1) * 60) + 59 - m1

    for num, time in sorted(times.items()):
        answer.append(fees[1])
        if time > fees[0]:
            time -= fees[0]
            addfees = time // fees[2]
            if time % fees[2]:
                addfees += 1
            answer[-1] += (addfees * fees[3])
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))

'''
구현 문제 인데 머리 속으로 생각은 하는데 코드로 잘 안 짜져서 적당히 고민 하고 검색 해서 풀었다.(처음엔 리스트로 풀다가 딕셔너리가 편할 거 같아서 바꿨고, 최대한 라이브러리 안 쓰는 코드를 찾았다)

collection 라이브러리에서 defaultdict를 사용 한다.
주차된 차들을 담는 cars를 딕셔너리로 선언 하고, 시간을 담아줄 times를 defaultdict(int)로 선언 한다.(int는 초기 값을 0으로 반환 해준다.)
records를 돌면서 담겨 있는 시간, 차량 번호, 상태를 split으로 따로 담아 준다(이거 돌면서 담는건 생각 못했다. 리스트로 끊어줄 생각만 함)
상태가 IN이면 cars에 차량 번호와 시간을 담는다(cars[num] = time 이렇게 담으면 num:time 이렇게 담기는 거 처음 알았다. 새로운 거 많이 배움)
OUT이면 시간 계산하려고 map을 사용해 int로 바꾸고, cars의 차량 번호의 시간을 시, 분으로 쪼갠다.
나간 시간도 똑같이  map을 사용해 int로 바꾸고, cars의 차량 번호의 시간을 시, 분으로 쪼갠다.
시끼리 빼고 분으로 환산해 분끼리 뺀 값과 더하고, times에 차량 번호와 넣는다.(여기 times[num]-차번호 안 써줘서 한참 해맸음)
times에 분으로 환산된 값을 넣어서 cars에 있는 값은 지운다.

cars에 값이 있으면 out이 안 된 차니까 cars.items()를 돌면서 차량 번호, 시간을 가져와
map을 사용해 int로 바꾸고, cars의 차량 번호의 시간을 시, 분으로 쪼갠다.
23시에서 시를 빼고 분으로 환산해 59분에서 분을 뺀 값과 더하고, times에 차량 번호와 넣는다.

작은 차번호 순서로 리턴 해야 돼서 sorted로 정렬된 times.items()를 돌건데 차량 번호, 시간을 가져 온다.
answer에 기본 요금을 넣고,
이용 시간이 기본 시간보다 크면
이용 시간에서 기본 시간을 빼고
추가 요금을 추가 시간 계산한 시간으로 선언한 뒤
추가 요금을 계산할 떄 나머지가 있으면 추가 요금에 1을 더한다.(나누어 떨어지지 않으면 무조건 올림 이라는 조건이 있어서)
answer에 마지막에 추가 요금 계산한 금액을 더해 준다.(마지막에 하는 이유는 처음에 answer에 기본 요금을 넣어서) 
'''