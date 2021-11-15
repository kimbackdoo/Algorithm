# LRU(Least Recently Used) 알고리즘을 이해하면 풀 수 있는 문제
# 이름에서 알 수 있듯이 가장 오랫동안 사용하지 않은 캐시를 교체하면 됨
# 캐시에 공간이 남아 있거나 없으면 캐시 miss, 공간이 남아 있으면 append, 남은 공간이 없으면 가장 오래된 요소 pop 후 해당 요소 append
# 캐시에 넣으려는 값이 이미 있으면 hit, 해당 요소를 가장 최신으로 갱신

# def solution(cacheSize, cities):
#     if cacheSize == 0: # cacheSize가 0이면 모든 요소 miss 이므로 len(cities) * 5 return
#         return len(cities) * 5
    
#     answer = 0
#     cache = []
#     for city in cities: # cities 모든 요소 순회
#         city = city.lower() # 대소문자 구문하지 않기 때문에 소문자로 변환
        
#         if city not in cache: # cache에 city가 없으면 miss
#             if len(cache) >= cacheSize: # cache 길이가 cacheSize보다 크거나 같으면 더 넣을 수 없으므로
#                 cache.pop(0) # 가장 오래된 요소 pop
                
#             cache.append(city) # city append
#             answer += 5 # miss일 때 시간 계산
        
#         else: # cache에 city가 있으면 hit
#             cache.append(cache.pop(cache.index(city))) # city 요소 가장 최신으로 갱신
#             answer += 1 # hit일 때 시간 계산
    
#     return answer

# 리스트를 사용하지 않고 deque 사용

# from collections import deque

# def solution(cacheSize, cities):
#     if cacheSize == 0:
#         return len(cities) * 5
    
#     answer = 0
#     cache = deque([])
#     for city in cities:
#         city = city.lower()
        
#         if city not in cache:
#             if len(cache) >= cacheSize:
#                 cache.popleft()
                
#             cache.append(city)
#             answer += 5
        
#         else:
#             cache.remove(city) # 해당 요소 remove
#             cache.append(city) # 해당 요소 append
#             answer += 1
    
#     return answer

# deque의 인자로 maxlen을 설정하여 deque의 크기가 maxlen을 넘어가지 않도록 함, 이렇게 하여 불필요한 연산 줄임

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize) # maxlen의 값을 cacheSize로 설정하여 cache 크기가 cacheSize로 되게함
    for city in cities:
        city = city.lower()
        # cache의 크기가 cacheSiz 값보다 큰지 확인하는 과정이 필요없음
        if city not in cache:
            cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
    
    return answer
