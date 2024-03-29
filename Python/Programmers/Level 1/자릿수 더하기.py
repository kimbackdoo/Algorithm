# def solution(n):
#     answer = list(str(n)) # 문자열로 변환 후 리스트로 변환
#     return sum([int(num) for num in answer]) # 각 요소가 각 자리수이므로 다시 int로 변환 후 합을 계산

# def solution(n):
#     # 문자열로 변환하고 리스트로 다시 변환할 필요 없음
#     return sum([int(num) for num in str(n)]) # n을 문자열 변환 후 한 개씩 int형으로 변환 후 합 계산

def solution(n):
    # n을 str로 변환 후 map 함수를 이용하여 모든 요소를 int로 바꾼 이터네리터로 변환 후 sum 함수를 이용하여 n의 모든 자리수 더하기
    return sum(map(int, str(n)))
