# s를 공백을 기준으로 나눈 후 int와 mapping 한 결과를 리스트로 변환

def solution(s):
    numbers = list(map(int, s.split(" "))) # s를 공백을 기준으로 split 후 int와 mapping 한 결과를 numbers에 저장
    return str(min(numbers)) + " " + str(max(numbers)) # numbers의 최솟값과 최댓값 반환
