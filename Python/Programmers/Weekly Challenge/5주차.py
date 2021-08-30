# A, E, I, O, U로 만들 수 있는 중복 순열을 구하고 word를 찾음

# from itertools import product

# def solution(word):
#     answer = []
#     for i in range(1, 6):
#         answer.extend(list(map("".join, product("AEIOU", repeat=i)))) # product 모듈을 이용하여 A, E, I, O, U로 만들 수 있는 모든 중복 순열을 answer에 저장
    
#     return sorted(answer).index(word) + 1 # answer를 오름차순 정렬 후 word를 찾음

# index 메소드를 이용하여 리스트 전체를 찾는 것이 아닌 bisect 모듈을 이용하여 이분탐색

# from itertools import product
# from bisect import bisect

# def solution(word):
#     answer = []
#     for i in range(1, 6):
#         answer.extend(list(map("".join, product("AEIOU", repeat=i))))
    
#     return bisect(sorted(answer), word) # bisect 모듈을 이용하여 정렬된 answer에서 word의 인덱스를 이분탐색으로 찾음

# dfs 알고리즘을 사용하여 완전 탐색으로 A, E, I, O, U로 만들 수 있는 모든 경우를 찾음

# def solution(word):
#     def dfs(p): # dfs 알고리즘 구현
#         if len(p) > 5: # A, E, I, O, U로 만들 수 있는 모든 경우이므로 길이가 5보다 크면 return 즉, 재귀 탈출
#             return
        
#         answer[p] = cnt[0] # 각각의 경우에서 p가 몇번째 위치하는지는 answer 딕셔너리에 저장
#         cnt[0] += 1 # 경우를 구할 때마다 cnt의 값 1 증가
        
#         for w in "AEIOU": # A, E, I, O, U로 만들 수 있는 모든 경우 dfs 탐색
#             dfs(p + w)
    
#     cnt = [0] # 해당 경우가 몇번째 위치하는지 확인할 리스트, 리스트는 주소가 참조 되므로 global 키워드 사용안해도 됨, 단순히 변수를 사용하려면 global 키워드 사용해야함
#     answer = {} # 각각의 경우에 몇번째 위치하는지 저장하기 위한 딕셔너리 즉, key는 각각의 경우, value는 해당 경우가 몇번째 위치하는지 숫자
#     dfs("") # dfs 탐색 시작
    
#     return answer[word] # answer에서 word가 몇번째 위치하는지 return

# dfs, 이분탐색 알고리즘을 구현하여 탐색

def solution(word):
    def dfs(p, word): # dfs 알고리즘 구현
        if len(p) > 5: return
        if p: answer.append(p)
        
        for w in "AEIOU":
            dfs(p + w, word)
    
    def binary_search(start, end): # 이분탐색 알고리즘 구현
        while start <= end:
            mid = (start + end) // 2

            if answer[mid] == word: # answer[mid]가 word와 같다면 해당 인덱스 +  1 return
                return mid + 1
            elif answer[mid] > word: # answer[mid]가 word보다 크다면 end 값을 줄임
                end = mid - 1;
            else: # answer[mid]가 word보다 작다면 start 값을 늘림
                start = mid + 1;
    
    answer = []
    dfs("", word) # dfs 탐색
    
    return binary_search(0, len(answer) - 1) # 이분탐색을 통해 word의 위치를 찾음
