# people을 오름차순 정렬 후 people의 제일 작은 값과 제일 큰 값을 더하여 limit보다 작거나 같으면
# 구명보트에 2명 모두 태우고, limit보다 크다면 제일 큰 값을 구명보트에 태워나가면 구명보트를 최소한으로 사용할 수 있음, 그리디 알고리즘 적용

def solution(people, limit):
    people.sort()
    left, right = 0, len(people)-1
    answer = 0
    while left <= right:
        if people[left] + people[right] <= limit: # people[left] + people[right]이 limit보다 작거나 같으면 즉, 2명을 구명보트에 모두 태울 수 있으면 
            left += 1 # left 값 +1 증가
            
        right -= 1 # people[right] 값은 항상 구명보트에 태워야하므로 계속해서 -1 감소
        answer += 1 # 구명보트 개수 count
    
    return answer
