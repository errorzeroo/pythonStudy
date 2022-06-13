word = input().upper()  # input 받는것을 list로 받고 대문자로 바꾼다.
word_set = set(word)  # word를 새로운 set으로 바꾼다.
word_set = list(word_set)  # set을 다시 list로 바꾼다.
word_cnt = list()  # count 받을 list를 새로 만든다.

for i in word_set:  # set으로 받은 리스트를 for에 넣어준다.
    cnt = word.count(i)  # for문에서 돌아가는 문자를 처음받은 문자의 수로 cnt변수로 받아준다.
    word_cnt.append(cnt)  # 빈 count 리스트에 추가 해준다.

if len(word_cnt) == 1:  # input을 1개만 받았을 때 그대로 프린트 해준다.
    print(word)
else:
    max_cnt = max(word_cnt)  # count된 단어 수가 1개가 아니면 ? 출력
    if word_cnt.count(max_cnt) > 1:
        print('?')
    else:
        print(word_set[word_cnt.index(max_cnt)])  # set의 인덱스가 cnt의 인덱스가 max인 것을 출력