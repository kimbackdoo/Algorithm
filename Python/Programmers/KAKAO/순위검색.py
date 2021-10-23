# 주어진 조건대로 조건에 해당하는 사람들의 수를 세면됨
# 처음에 단순히 순차탐색으로 풀었지만 효율성에서 오답, 최악의 경우 10^5 * 5 * 10^4 = 5 * 10^9 이므로 시간초과남
# 조건에 맞는 사람들 중 주어진 코딩테스트의 점수 이상인 사람들의 수를 찾으면 되므로 이진탐색 알고리즘 중 lower bound 알고리즘 사용
# lower bound 알고리즘: 리스트에서 x이상이 되는 첫번째 인덱스를 찾음
# upper bound 알고리즘: 리스트에서 x보다 큰 즉, x 초과인 첫번째 인덱스를 찾음

# from collections import defaultdict

# def binary_search(scores, target): # 이진탐색 중 lower bound 알고리즘 구현
#     # end값이 len(scores) - 1이 아니라 len(scores)인 이유는 target이 scores의 모든 요소보다 클 수도 있기 때문
#     # scores의 모든 요소보다 클 경우 len(scores)의 값이 반환됨
#     start, end = 0, len(scores)
#     while start < end: # start의 값이 end 값보다 작은 경우 반복
#         mid = (start + end) // 2 # mid 값 계산
        
#         if scores[mid] >= target: # mid번째 요소의 값이 target보다 클 경우
#             end = mid # end 값 mid 값으로 변경, 이때 end = mid - 1이 아닌 이유는 mid 값이 target 이상이 되는 첫번째 인덱스일수도 있기 때문
#         else: # 작을 경우
#             start = mid + 1 # start 값 증가
    
#     return start # start 값 return

# def solution(info, query):
#     applicant = defaultdict(list) # 점수를 제외한 부분을 key, 점수를 value로 설정하기 위한 dic, 이때 점술를 제외한 부분이 겹칠 수 있으므로 defaultdict 모듈을 이용하여 value가 리스트가 되게함
#     for i in info: # info의 모든 요소 순회
#         i = i.split()
#         applicant[" ".join(i[:-1])].append(int(i[-1])) # 점수가 아닌 부분을 key로 설정하고 점수를 append
    
#     for key in applicant: # 이진탐색 알고리즘을 사용하기 위해 value 리스트를 오름차순 정렬시킴
#         applicant[key].sort()
        
#     answer = []
#     for q in query: # query의 모든 요소 순회
#         q = q.replace("-", "").replace("and", "").split() # q에서 _, and 부분을 없애고 배열로 변환
#         cnt = 0 # 사람들의 수를 세기 위한 변수
#         for key, value in applicant.items(): # applicant 딕셔너리를 (key, value) 리스트로 변환 후 모든 요소 순회
#             if (set(q[:-1]) - set(key.split())) == set(): # 점수가 아닌 부분들의 차집합이 공집합이면 즉, 조건에 맞는 경우
#                 idx = binary_search(value, int(q[-1])) # 해당 조건의 점수 이상인 사람들을 찾기 위해 이진탐색
#                 cnt += (len(value) - idx) # 해당 value 리스트의 크기에서 idx값을 빼면 조건을 만족하는 사람들의 숫자이므로 count
                
#         answer.append(cnt)
    
#     return answer

from collections import defaultdict
from itertools import combinations

def binary_search(scores, target):
    start, mid, end = 0, 0, len(scores)
    while start < end:
        mid = (start + end) // 2

        if scores[mid] >= target:
            end = mid
        else:
            start = mid + 1

    return start

def solution(info, query):
    db = defaultdict(list)
    for i in info:
        i = i.split()
        score = int(i[-1])
        applicant = i[:-1]
        for pick in range(5):
            for combi in list(combinations(range(4), pick)):
                tmp = applicant[:]
                for c in combi:
                    tmp[c] = "-"

                db[" ".join(tmp)].append(score)

    for key in db:
        db[key].sort()

    answer = []
    for q in query:
        que = q.replace("and", "").split()
        score = int(que[-1])
        que = " ".join(que[:-1])
        if que in db:
            idx = binary_search(db[que], score)
            answer.append(len(db[que]) - idx)
        else:
            answer.append(0)

    return answer
