room, nums = map(int, input().split())
timeslot = [[0 for i in range(9)] for i in range(50)]
room_list = []
for i in range(room):
    room_list.append(input())
room_list.sort()
for i in range(nums):
    room_name, time_s, time_e = input().split()
    time_s, time_e = int(time_s)-9, int(time_e)-9
    for j in range(time_s, time_e):
        timeslot[room_list.index(room_name)][j] = 1
for i in range(room):
    print(f'Room {room_list[i]}:')
    if 0 not in timeslot[i]:
        print('Not available')
    else:
        temp = 1
        reservation = []
        for idx, j in enumerate(timeslot[i]):
            if j != temp:
                reservation.append(idx+9)
                temp = j
        if j == timeslot[i][-1] == 0:
            reservation.append(18)
        if reservation[0] == 9:
            reservation[0] = '09'
        print(len(reservation)//2, 'available:')
        for rsv in range(0, len(reservation), 2):
            print(reservation[rsv], '-', reservation[rsv+1], sep='')
    if i != room-1:
        print('-----')

'''
01: 방의 개수와 예약된 시간의 수를 인풋 받는다
02: 방별로 예약할 시간을 리스트로 초기화 해준다. (방이 최대 50개여서 50개의 리스트)
    [[0*9]*50] 9는 시간대, 50은 방의 개수
03: 방의 이름을 넣을 리스트를 초기화해준다.
04: 방의 개 수만큼 for문을 돌면서
05: 인풋 받은 방의 이름을 리스트에 넣어 준다.
06: 방이름 리스트를 알파벳 순으로 정렬 한다.
07: 예약된 수만큼 for문을 돌면서
08: 방이름, 예약 시작 시간, 끝 시간을 인풋 받는다
--09: 예약 시간을 int로 변환 하고, 인덱스 수를 맞추기 위해 -9를 한다.
--10: 시작 시간부터 끝 시간까지 i가 돌 동안 j를 반복
11: 인풋 받은 방이름을 방이름 리스트에 인덱스로 가져와 시간 리스트에 j를 1로 바꾼다.(예약된 시간 표시)
12: 출력 방 개 수만큼 for문
13: Room i번째방이름: 출력
14: 만약 시간 리스트 i번째 리스트에 0이 없으면 빌릴 방이 없으므로
15: Not available을 출력
16: 예약할 수 있으면
17: 비교할 변수 생성
18: 예약 되는 리스트를 생성
19: 시간 리스트에 첫번재 i의 리스트를 인덱스와 값으로 for문을 돌면서
20: 값이 비교할 변수와 다르면 값을 
24: --개수 만큼의 방이 available: 을 출력

28: 만약 마지막 방이 아니면
29: -----를 출력
'''