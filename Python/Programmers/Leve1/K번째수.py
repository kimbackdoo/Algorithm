def sort(arr): # 정렬 구현
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
    return arr
    
def solution(array, commands):
    answer = []
    for command in commands:
        arr = array[command[0]-1 : command[1]]
        arr = sort(arr)
        answer.append(arr[command[2]-1])
    return answer
