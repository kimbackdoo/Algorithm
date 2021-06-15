# permutations 라이브러리를 이용하여 종이조각을 이용한 모든 숫자 조합을 구함
# 순열의 중복을 제거하고 소수의 개수를 찾음
# 순열 : 순서를 고려하므로 A, B, C에서 2개의 원소를 고를 때 (A, B), (B, A)는 같은 것
# 조합 : 순서를 고려하지 않으므로 A, B, C에서 2개의 원소를 고를 때 (A, B), (B, A)는 다른 것

# from itertools import permutations

# def check(num): # 소수 체크
#     if num == 0 or num == 1:
#         return False
    
#     for i in range(2, int(num**0.5)+1): # 매개변수로 들어온 num의 제곱근까지만 확인하여 속도 높임
#         if num % i == 0:
#             return False
        
#     return True

# def set(nums): # set 구현 즉, 중복 제거
#     result = []
#     for num in nums:
#         if num not in result: # 중복되지 않으면 append
#             result.append(num)
            
#     return result

# def solution(numbers):
#     numbers = list(numbers)
    
#     nums = []
#     for i in range(1, len(numbers)+1):
#         p = list(permutations(numbers, i)) # 나올 수 있는 모든 순열을 구함
#         for j in range(len(p)):
#             num = "".join(p[j]) # 구한 순열마다 문자열로 변환하고
#             nums.append(int(num)) # nums 리스트에 append
    
#     nums = set(nums) # 중복 제거
#     answer = 0
#     for num in nums:
#         if check(num): # 소수 체크
#             answer += 1
            
#     return answer

from itertools import permutations

def isPrime(num): # 소수 체크
    chk = num ** 0.5 # 제곱근까지만 체크

    if num < 2: return False

    for i in range(2, int(chk)+1):
        if num % i == 0: return False

    return True

def solution(numbers):
    answer = []

    for p in range(1, len(numbers) + 1):
        primeList = list(map(''.join, permutations(list(numbers), p))) # 나올 수 있는 모든 순열에 대해 문자열로 변환

        for prime in list(set(primeList)): # 구한 문자열 리스트 중복제거
            if isPrime(int(prime)): # int로 변환 후 소수 체크
                answer.append(int(prime)) # answer에 append

    return len(set(answer)) # 중복 제거 후 길이가 최종 소수의 개수가 됨
