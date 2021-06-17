# skill_trees에 각 skill_tree에서 각 기술의 위치를 찾는다.
# 만약 선행 기술이 포함되어 있지 않으면 skill_tree의 길이를 저장한다.
# 이유는 예를 들어, skill_tree의 길이가 5이고, B -> C -> D 순서로 스킬을 배워야 한다면
# B -> C 먼저 배우고 D를 안배운다면 [B의 위치, C의 위치, 5]가 되고
# B -> D 순서로 스킬을 배운다면 [B의 위치, 5, D의 위치]가 된다.
# 즉, 리스트가 정렬되어 있으면 선행 스킬 순서가 올바른 것이고 정렬되어 있지 않으면 선행 스킬을 배우지 않은 것이 됨

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees: # skill_trees에서 각 skill_tree를 확인
        check = [] # 선행 스킬 순서가 올바른지 확인하기 위한 리스트
        for word in skill:
            if word in skill_tree: # skill_tree에 스킬이 포함되어 있다면
                check.append(skill_tree.find(word)) # 해당 스킬의 위치를 찾아 append
            else: # 포함되어 있지 않다면
                check.append(len(skill_tree)) # skill_tree의 길이를 append, 이유는 정렬을 확인하기 위함 
                
        if check == sorted(check): # 정렬되어 있다면 선행 스킬 순서가 올바른 것이고, 정렬되어 있지 않다면 선행 스킬 순서가 올바르지 않은 
            answer += 1
            
    return answer
