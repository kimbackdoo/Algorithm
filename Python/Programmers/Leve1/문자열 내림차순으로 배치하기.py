def sort(s, reverse): # 정렬 구현, reverse에 따라 True면 내림차순, False면 오름차순
    for i in range(len(s)):
        for j in range(i, len(s)):
            if reverse:
                if ord(s[i]) < ord(s[j]):
                    s[i], s[j] = s[j], s[i]
            else:
                if ord(s[i]) > ord(s[j]):
                    s[i], s[j] = s[j], s[i]

    return s

def solution(s):
    return "".join(sort(list(s), True)) # 정렬 후 문자열 반환
