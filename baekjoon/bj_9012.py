# 괄호
test_case = int(input())
bracket = []
for ip in range(test_case):
    bracket.append(input())

for pr in range(test_case):
    if bracket[pr][0] == ")":
        print("NO")
    elif bracket[pr][-1] == "(":
        print("NO")
    else:
        if len(bracket[pr]) % 2 == 1:
            print("NO")
        else:
            left = 0
            right = 0
            for cnt in bracket[pr]:
                if cnt == '(':
                    left += 1
                else:
                    right += 1
                    if right > left:
                        break
                        print("NO")
            if left == right:
                print("YES")
            else:
                print("NO")

'''
programmers 올바른 괄호 참고 했다
test_case를 입력 받고
빈 리스트를 만든다
test_case만큼 for문 돌면서 입력 받은 괄호를 bracket에 추가
bracket을 돌면서 괄호가 올바른지 확인 한다. --programmers stackQueue rightBracket 참고
'''