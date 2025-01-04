// 현재 학생이 체육복을 빌려줄 수 있는지 없는지 체크 => 그리디 알고리즘 적용
// 여벌 체육복을 가지고 온 학생이 체육복을 잃어버린 경우는 본인이 입어야 하므로 lost, reserve 배열에서 각각 차집합을 구함
// 학생 번호 -1, +1인 경우에 해당하면 체육복을 빌려줌

// function solution(n, lost, reserve) {
//     let diffLost = lost.filter(number=> !reserve.includes(number)); // lost와 reserve의 차집합을 구함
//     let diffReserve = reserve.filter(number=> !lost.includes(number)); // reserve와 lost의 차집합을 구함
    
//     diffReserve.forEach(number=> { // forEach 메소드를 사용하여 diffReserve의 모든 요소를 순회
//         if (diffLost.indexOf(number - 1) !== -1) { // number - 1이 diffLost에 있다면
//             diffLost.splice(diffLost.indexOf(number - 1), 1); // 체육복을 빌려줌
//         } else if (diffLost.indexOf(number + 1) !== -1) { // number + 1이 diffLost에 있다면
//             diffLost.splice(diffLost.indexOf(number + 1), 1); // 체육복을 빌려줌
//         }
//     });
    
//     return n - diffLost.length; // 전체 학생 수에서 빌리지 못한 학생 수를 빼면 정답
// }

// function solution(n, lost, reserve) {
//     const filteredLost = lost.filter((number) => !reserve.includes(number)).sort()
//     const filteredReserve = reserve.filter((number) => !lost.includes(number)).sort()
//     const reserveObj = Object.fromEntries(filteredReserve.map((number) => [number, true]))
    
//     let answer = n - filteredReserve.length
//     filteredLost.forEach((number) => {
//         const nextNumber = !!reserveObj[number - 1] ? number - 1 : !!reserveObj[number + 1] ? number + 1 : -1
//         if (nextNumber === -1) return
        
//         answer += 1
//         reserveObj[nextNumber] = false
//     })
    
//     return answer
// }

function solution(n, lost, reserve) {
    const answer = Array(n).fill("O")
    lost.forEach((number) => answer[number - 1] = "L")
    reserve.forEach((number) => answer[number - 1] = answer[number - 1] === "L" ? "O" : "R")
    
    for (let i = 0; i < n; i++) {
        if (answer[i] !== "L") continue
        
        if (answer[i - 1] === "R") {
            [answer[i], answer[i - 1]] = ["O", "O"]
        } else if (answer[i + 1] === "R") {
            [answer[i], answer[i + 1]] = ["O", "O"]
        }
    }
    
    return answer.filter((status) => status !== "L").length
}