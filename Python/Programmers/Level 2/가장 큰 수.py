# numbers의 원소는 1000이하의 숫자이므로 각 원소를 str을 이용하여 문자열로 변환 후 *4 하여 길이를 4이상으로 늘림
# 모든 원소가 1000이하이므로 길이가 4가 되도록 split
# zip을 이용하여 묶어서 정렬 후 가장 큰 수를 만들어냄

def solution(numbers):
    if numbers.count(0) == len(numbers): # 모든 원소가 0으로 이루어진 경우 0을 반환
        return "0"
    
    s = []
    for number in numbers:
        num = str(number) * 4 # 모든 원소의 길이를 4 이상으로 늘림
        s.append(num[:4]) # 길이가 4가 되도록 split
        
    tmp = list(zip(s, numbers)) # zip을 이용하여 s, numbers을 묶고
    tmp.sort(reverse=True) # 역순 정렬 진행
    
    answer = ""
    for t in tmp:
        answer += str(t[1]) # tmp의 각 원소의 두번째 요소가 원래 숫자이므로 각 원소를 answer에 이어 붙임 
    
    return answer
