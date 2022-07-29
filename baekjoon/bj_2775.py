# 부녀회장이 될테야
test_case = int(input())
for i in range(test_case):
    floor_list = [list(range(1, 15))]
    floor = int(input())
    ho = int(input())
    for j in range(1, floor):
        live_ho = []
        for h in range(1, ho+1):
            live_ho.append(sum(floor_list[j-1][:h]))
        floor_list.append(live_ho)
    print(sum(floor_list[floor-1][:ho]))

'''
테스트 케이스를 받는다
테스트 케이스만큼 for문을 돌건데 돌때마다 층수와 호수를 인풋 받는다
층수에 대한 for문 안에서 호수 리스트를 만들건데 호수 리스트를 for문들 돌면서 저장한다
호수 리스트(live_ho)는 현재 층에서 현재 호수 까지를 더한 것을 저장
호수 리스트를 층수 리스트에 저장한다.
인풋 받은 호수의 사는 사람 출력-전층의 호수까지 사는 사람을 더한 값

포인트 : 처음 0층은 1-14까지 있다.(초기값 설정)
포인트 : 초값에 2차원 배열을 만든다.[[0층], [1층], [2층], ***, [14층]]
포인트 : [1층]을 만드는 게 0층에서 현재 j-1에서 현재 h까지 더한 수를 []에 넣는다
'''