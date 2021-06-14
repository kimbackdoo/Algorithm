# 그리디 알고리즘 : 선택의 순간 최적의 해를 찾는 알고리즘
# 입력받은 걸리는 시간 리스트를 정렬하여 누적 시간이 최소로 되게 만듦
# 각 사람이 인출할 수 있는 시간을 이중 for문으로 순회하면서 계산

# n = int(input())
# m = list(map(int, input().split()))

# m.sort()
# result = 0
# for i in range(1, n):
#   tmp = 0
#   for j in range(i):
#     tmp += m[j]
    
#   result += tmp

# print(result + sum(m))

n = int(input())
m = list(map(int, input().split()))

if n == 1: # n이 1일 경우는 한가지 밖에 없으므로 바로 출력
    print(m[0])
else : 
    nums.sort()

    result, tmp = 0, 0
    # tmp에 현재 시간 전까지의 시간들을 저장해두고 result에 현재 시간 + tmp를 하여 최종 걸린 시간을 구함
    # 이렇게 하면 이중 for문을 사용하지 않아도 되므로 속도 향상
    for i in range(n): 
        result += (tmp + m[i])
        tmp += m[i]
        
    print(min_sum)
