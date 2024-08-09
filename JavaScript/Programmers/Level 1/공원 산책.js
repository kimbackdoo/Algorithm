// routes 따라가면서 이동한 후의 위치를 반환하는 문제
// 공원을 벗어나거나 장애물을 만나면 패스
function solution(park, routes) {
    const direction = { E: [0, 1], S: [1, 0], W: [0, -1], N: [-1, 0] }
    
    let startY = park.findIndex((item) => item.includes("S"))
    let startX = park[startY].indexOf("S")
    
    routes.forEach((route) => {
        const [op, n]  = route.split(" ")
        let [tmpY, tmpX] = [startY, startX]
        
        for(let i = 0; i < n; i++) {
            [tmpY, tmpX] = [tmpY + direction[op][0], tmpX + direction[op][1]]
            
            if (!park[tmpY] || !park[tmpY][tmpX] || park[tmpY][tmpX] === "X") {
                return
            }
        }
        
        [startY, startX] = [tmpY, tmpX]
    })
    
    return [startY, startX];
}