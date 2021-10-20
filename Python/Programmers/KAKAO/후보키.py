# 후보키의 조건인 유일성과 최소성을 만족하는 경우의 개수를 모두 구하면 됨
# 예를 들어, [1, 2], [1, 2, 4] 중에서는 [1, 2]가 후보키가 된다. 이유는 [1, 2, 4]는 최소성을 만족하지 못하기 때문이다.
# combinations 모듈을 사용하지 않고 백트래킹 알고리즘을 사용하여 가지치기로 경우의 수를 구함
# 1부터 1로 만들 수 있는 모든 경우를 확인하게 되면 최소성을 확인하지 못하므로 조합이 1개인 경우부터 확인함

def solution(relation):
    def dfs(length, idx, combi, pick): # 백트래킹 알고리즘을 위해 dfs 구현
        if len(combi) == pick: # 뽑는 개수와 뽑힌 조합의 개수가 같다면
            check = True
            # answer에는 조합이 1개인 경우부터 차례대로 담김
            # candidate는 이미 후보키로 뽑힌 경우이므로 candidate와 combi의 차집합이 공집합일 경우 최소성을 만족하지 못하는 경우
            for candidate in answer:
                if set(candidate) - set(combi) == set(): # candidate와 combi의 차집합을 했을 경우는 최소성을 만족하지 못함
                    check = False # check False로 변환
                    break
            
            if check: # 최소성을 만족하였으면
                candidate_key = []
                for i in range(len(relation)):
                    tmp = []
                    for j in combi:
                        tmp.append(relation[i][j])

                    candidate_key.append(tuple(tmp)) # 튜플을 유일하게 식별할 수 있는지 확인하기 위하여 relation에서 combi의 column을 뽑아냄

                if sorted(candidate_key) == sorted(set(candidate_key)): # 뽑힌 column과 column에서 중복을 제거했을때와 같다면 즉, 유일성을 만족하면
                    answer.append(combi) # 최소성과 유일성을 모두 만족한 것이므로 answer의 후보키 append
                
            return

        for i in range(idx, length): # relation의 column 크기만큼 dfs 탐색
            dfs(length, i + 1, combi + [i], pick)
    
    answer = []
    for i in range(1, len(relation[0]) + 1): # 조합의 개수가 1개부터 relation의 column 개수까지 차례대로 조합을 구함
        dfs(len(relation[0]), 0, [], i)

    return len(answer) # 최종 후보키의 개수 return
