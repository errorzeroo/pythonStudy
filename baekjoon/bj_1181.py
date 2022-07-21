# 단어 정렬
word_len = int(input())              # 알파벳 갯수 인풋
word_dict = {}                       # 알파벳 넣을 딕셔너리
for word in range(word_len):         # word_len 만큼 for문 돌림
    word = input()                   # 알파벳 인풋 받음
    value = len(word)                # 알파벳의 길이
    word_dict.update({word:value})   # 알파벳과 알파벳 길이를 딕셔너리에 저장
word_dict = sorted(word_dict.items(), key=lambda x: x[0])  # 알파벳 기준으로 정렬
word_dict = sorted(word_dict, key=lambda x: x[1])  # 길이 기준으로 정렬
for i in word_dict:
    print(i[0])

# lambda는 함수, x는 word_dict의 모든 값을 돈다.
# 거기서 x[0]의 값을 기준으로 정렬 시킨다.
