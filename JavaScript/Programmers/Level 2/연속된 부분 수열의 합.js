function solution(sequence, k) {
    const answer = [0, sequence.length]
    let [tmp, right] = [0, 0]
    for (let i = 0; i < sequence.length; i++) {
        while (right < sequence.length && tmp < k) {
            tmp += sequence[right]
            right += 1
        }
        
        if (tmp === k && right - 1 - i < answer[1] - answer[0]) {
            [answer[0], answer[1]] = [i, right - 1]
        }
        
        tmp -= sequence[i]
    }
    
    return answer
}