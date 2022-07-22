# 블랙잭
num, score = map(int, input().split())       # 뽑을 카드 개수와 합칠 수 인풋
card_num = list(map(int, input().split()))   # 카드 인풋
card_list = []                               # 합친 카드 리스트
for i in range(len(card_num)):               # 첫번째 카드 for 문
    for j in range(i+1, len(card_num)):      # 두번째 카드 for 문
        for k in range(j+1, len(card_num)):  # 세번째 카드 for 문
            sum_card = card_num[i] + card_num[j] + card_num[k]  # 세카드 더하기
            if sum_card <= score:            # 합친 수를 넘지 않게
                card_list.append(sum_card)   # 합친 카드 리스트에 넣기
print(max(card_list))                        # 합친 수에 가장 가까운 수 출력
