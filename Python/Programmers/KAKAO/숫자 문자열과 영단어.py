# 해당 문자열을 숫자로 변환하면 됨
# 즉, zero는 0, one는 1, two는 2, ...
# dictonary를 사용하여 계산

def solution(s):
    # 숫자에 해당하는 문자열 딕셔너리 생성
    d = {"zero": "0", "one": "1", "two": "2",
              "three": "3", "four": "4", "five": "5",
              "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for number in d: # 딕셔너리 모든 key를 반복하면서 replace
        s = s.replace(number, d[number]) # 문자열을 해당하는 숫자로 변환
        
    return int(s)
