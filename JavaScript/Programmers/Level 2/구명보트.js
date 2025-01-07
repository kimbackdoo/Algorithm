function solution(people, limit) {
    people.sort((a, b) => a - b)
    
    let answer = 0
    let [left, right] = [0, people.length - 1]
    while (left <= right) {
        if ((people[left] + people[right]) <= limit) left += 1
        
        right -= 1
        answer += 1
    }

    
    return answer
}