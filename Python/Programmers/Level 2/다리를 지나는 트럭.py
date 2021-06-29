# 최소 시간을 구하는 것이므로 weight가 될 때까지 트럭을 올려야 됨
# 문제에 나온 표를 그대로 구현하면 됨
# 다리는 건너고 지나는 것을 큐로 구현
# 예를 들어, 대기 트럭이 [7,4,5,6]d이고, 무게가 10이라면 다리는 건너는 트럭을 표현하면 아래와 같다
# [0,0] -> [0] -> [0,7] -> [7] -> [7,0] -> [0] -> [0, 4] -> [4] -> [4,5] -> [5] -> [5,0] -> [0] -> [0,6] -> [6] -> []

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length # bridge_length 만큼 다리 리스트 생성
    answer = 0
    while bridge: # 모든 트럭이 지날 때까지 반복
        bridge.pop(0) # 트럭이 다리를 지남
        
        if truck_weights: # 대기 트럭이 남아있으면 
            if sum(bridge) + truck_weights[0] <= weight: # 다리를 건너는 트럭들의 합과 다리에 오를 트럭의 무게 합이 weight보다 작거나 같으면 즉, 다리에 오를 수 있으면
                truck = truck_weights.pop(0) # 대기 트럭의 요소를 pop
                bridge.append(truck) # 다리에 올림
            else: # 그렇지 않으면 즉, 다리에 오를 수 없으면
                bridge.append(0) # 0 append
        
        answer += 1
        
    return answer
