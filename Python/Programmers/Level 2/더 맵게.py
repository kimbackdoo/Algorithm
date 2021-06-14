# 섞은 음식의 스코빌 지수는 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)이므로 scoville는 항상 정렬되어 있어야 한다.
# 효율성 테스트를 통과하기 위해 리스트를 매번 정렬 시키는 것이 아닌 heapq 라이브러리를 사용하여 성능을 높임

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # scoville 리스트를 heap으로 변환
    while scoville[0] < K: # scoville의 첫번째 요소가 K보다 커지는 순간까지 반복
        if len(scoville) == 1: return -1 # scoville의 길이가 1개라는 의미는 K 이상으로 만들 수 없는 뜻이므로 -1 반환
            
        a = heapq.heappop(scoville) # 제일 작은 수 heappop
        b = heapq.heappop(scoville) # 두번째로 작은 수 heappop
        heapq.heappush(scoville, a + (b*2)) # 섞은 음식의 스코빌 지수 계산하여 heappush
        answer += 1
    
    return answer
