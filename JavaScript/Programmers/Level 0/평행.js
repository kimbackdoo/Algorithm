function solution(dots) {
    const [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    
    const case1 = Math.abs(y2 - y1) / Math.abs(x2 - x1) === Math.abs(y4 - y3) / Math.abs(x4 - x3)
    if (case1) return 1
    
    const case2 = Math.abs(y3 - y1) / Math.abs(x3 - x1) === Math.abs(y4 - y2) / Math.abs(x4 - x2)
    if (case2) return 1
    
    const case3 = Math.abs(y4 - y1) / Math.abs(x4 - x1) === Math.abs(y3 - y2) / Math.abs(x3 - x2)
    if (case3) return 1
    
    return 0
}