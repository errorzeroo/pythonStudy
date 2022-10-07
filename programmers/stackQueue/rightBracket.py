def solution(s):
    if s[0] == ")":
        return False
    elif s[-1] == "(":
        return False
    else:
        if len(s) % 2 == 1:
            return False
        else:
            left = 0
            right = 0
            for str in s:
                if str == '(':
                    left += 1
                else:
                    right += 1
                    if right > left:
                        break
                        return False
            if left == right:
                return True
            else:
                return False

'''
첫 괄호가 )로 시작 하면 false
끝 괄호가 (로 끝나면 false
괄호의 개수가 홀수이면 false
왼쪽 ( 오른쪽 )로 나눠서 for문으로 개수를 세는데
왼쪽 보다 오른쪽이 크면 break 후 false
for문이 다 돌고 개수가 같으면 true 다르면 false 
'''