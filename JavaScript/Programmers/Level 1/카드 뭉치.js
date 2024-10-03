function solution(cards1, cards2, goal) {
    for (const target of goal) {
        if (target === cards1[0]) {
            cards1.shift()
            continue
        }
        
        if (target === cards2[0]) {
            cards2.shift()
            continue
        }
        
        return "No"
    }
    
    return "Yes"
}