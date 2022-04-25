# h-index => 역순 정렬 후 max(f(n) >= i)
# 즉, f(n)이 i랑 같거나 작아지는 순간이 h-index가 됨

def solution(citations):
    citations.sort(reverse=True) # h-index를 구하기 위해 역순 정렬
    for i in range(len(citations)):
        if citations[i] <= i: # 공식 적용 즉, citations[i] 값이 i랑 같거나 작아지는 순간이 h-index
            return i
          
    return len(citations) # 만약 citations[i] 값이 i랑 같거나 작아지는 순간이 없다면 citations 길이가 h-index가 됨
