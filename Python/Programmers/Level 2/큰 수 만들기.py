# 가장 큰 수를 만들기 위해서는 앞자리가 제일 큰수여야 함
# 반복문과 stack을 사용하여 각 자리가 제일 큰 수가 되게 만든다.
# answer의 마지막 값보다 num이 크다면 더 큰 수를 만들 수 있는 것이므로 answer의 마지막 값이 num 보다 크지 않을 때까지 반복문을 통해 pop 연산
# 이때 삭제할 수 있는 개수인 k의 값을 -1씩 감소시키면서 만약 k번 제거 되었으면 반복문을 돌지 않게 함

def solution(number, k):
    answer = []
    for num in number:
        # 각 자리의 수를 가장 크게 만든다.
        # pop 할 때마다 k의 값 -1씩 감소
        # 예를 들어, "4177252841"이라면 앞에서부터 비교해가기 때문에 7이 answer에 담기고 number의 모든 수를 k번 제거할 때까지 비교한다.
        while answer and answer[-1] < num and k > 0:
            answer.pop()
            k -= 1
            
        answer.append(num) # k의 값이 0 이하이거나 answer의 마지막 값이 num보다 크거나 같다면 append
    
    if k > 0: # 만약 모든 비교를 했는데 k의 값이 0보다 클 경우
        answer = answer[:-k] # answer에서 -k만큼 split 시켜 남은 수를 제거하여 가장 큰 수를 만든다.
    
    return "".join(map(str,answer))
