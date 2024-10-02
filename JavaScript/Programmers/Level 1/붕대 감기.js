function solution(bandage, health, attacks) {
    const [t, x, y] = bandage
    
    let start = 0
    let answer = health
    
    for (const [time, damage] of attacks) {
        if (answer <= 0) return -1
        
        const period = (time - start - 1)
        const physical = answer + x * period + y * Math.floor(period / t)
        answer = Math.min(physical, health) - damage
        start = time
    }
    
    return answer > 0 ? answer : -1 
}