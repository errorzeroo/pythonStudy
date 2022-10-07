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