# 2개의 dict을 만들고, 1개는 장르별로 재생횟수와 고유번호를 저장, 나머지 1개는 장르별 총 재생횟수 저장
# 총 재생횟수가 높은 장르를 먼저 수록해야 하므로 역순 정렬
# 장르 내에서 같은 재생횟수이면 고유번호가 낮은 번호가 먼저 수록되어야 하므로 내림차순 정렬하되, 같을 경우 고유번호 기준 오름차순 정렬
# 장르에 속한 곡이 하나만 있을 수 있으므로 길이가 1일 때 아닐때 나누어서 생각

from collections import defaultdict

def solution(genres, plays):
    genre_dict = defaultdict(list) # 장르별 재생횟수와 고유번호를 저장할 dict
    sum_dict = defaultdict(int) # 장르별 총 재생횟수를 저장할 dict
    for i in range(len(genres)):
        genre_dict[genres[i]].append((plays[i], i)) # genre_dict에 재생횟수와 고유번호를 튜플로 저장
        sum_dict[genres[i]] += plays[i] # 장르별 총 재생횟수 저장
    
    for key in genre_dict.keys(): # 장르 내에서 재생횟수가 높을수록 먼저 수록되고, 같을 경우 고유번호를 기준으로 오름차순 정렬해야하므로 장르별로 반복
        genre_dict[key].sort(key=lambda x: (x[0], -x[1]), reverse=True) # lambda 사용하여 기본적으로 재생횟수를 기준으로 내림차순 정렬하고, 같을 경우 고유번호를 기준으로 오름차순 정렬
    
    answer = []
    # 총 재생횟수가 높은 장르를 먼저 수록해야 하므로 (key, value) 튜플에서 lambda를 사용하여 value를 기준으로 내림차순 정렬
    for key, value in sorted(sum_dict.items(), key=lambda x : x[1], reverse=True):
        # 장르별로 2곡씩 수록해야 하므로 장르에 속한 곡이 1개일 경우, 아닐 경우로 나누어 append
        if len(genre_dict[key]) != 1: # 장르에 속한 곡이 2개 이상일 경우
            answer.append(genre_dict[key].pop(0)[1]) # pop 연산 후 고유번호 append
            
        answer.append(genre_dict[key].pop(0)[1]) # 장르에 속한 곡이 1개일 경우에는 pop 연산 한 번만 수행
    
    return answer
