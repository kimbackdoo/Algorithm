# 섞은 음식의 스코빌 지수는 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)이므로 scoville는 항상 정렬되어 있어야 한다.
# 효율성 테스트를 통과하기 위해 리스트를 매번 정렬 시키는 것이 아닌 heapq 라이브러리를 사용하여 성능을 높임

# import heapq

# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville) # scoville 리스트를 heap으로 변환
#     while scoville[0] < K: # scoville의 첫번째 요소가 K보다 커지는 순간까지 반복
#         if len(scoville) == 1: return -1 # scoville의 길이가 1개라는 의미는 K 이상으로 만들 수 없는 뜻이므로 -1 반환
            
#         a = heapq.heappop(scoville) # 제일 작은 수 heappop
#         b = heapq.heappop(scoville) # 두번째로 작은 수 heappop
#         heapq.heappush(scoville, a + (b*2)) # 섞은 음식의 스코빌 지수 계산하여 heappush
#         answer += 1
    
#     return answer

from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville) # scoville을 최소힙으로 변환 
    while len(scoville) >= 2 and scoville[0] < K: # 2번의 pop 연산을 수행하므로 scoville의 크기는 2 이상이어야 하며, scoville[0]의 값이 K보다 작을때 반복
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2) # 스코빌 지수 섞기
        answer += 1
    
    return answer if scoville[0] >= K else -1 # scoville[0] 값이 K이상이면 answer, 아니면 -1 return
