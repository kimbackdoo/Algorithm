// 최대한 많은 부서에 예산을 지급해줘야 함, 즉, 예산이 제일 적은 부서부터 차례대로 예산을 지급해줌, 그리디 알고리즘 적용

// function solution(d, budget) {
//     let sum = 0;
//     return d.sort((a, b) => a - b) // 각 부서의 예산 오름차순 정렬
//         .filter(b => { // sum에 각 부서의 예산을 더해나감
//         sum += b;
//         if (sum > budget) // sum이 budget보다 크다면 더이상 예산을 지급해줄 수 없으므로 false return
//             return false;
        
//         return true; // 그게 아니라면 return true
//     }).length; // 필터링 된 배열에는 예산을 지급해줄 수 있는 부서만 남게 되므로 필터링 된 배열의 크기 return
// }

// filter 메소드의 매개변수로 콜백함수가 들어오므로 중간에 멈추지 않고 배열 전체를 순회하면서 true인 요소들만 배열에 남김
// d를 오름차순 정렬했으므로 배열 전체를 순회할 필요 없이 for문을 사용하여 예산을 지급해주다가 budget보다 큰 순간 순회를 멈춤

function solution(d, budget) {
    d = d.sort((a, b) => a - b);
    let idx, sum = 0;
    for (idx = 0; idx < d.length; idx++) {
        sum += d[idx];
        if (sum > budget) // 배열의 모든 요소를 순회하지 않고 sum이 budget보다 큰 순간 break
            break;
    }
    
    return idx; // break 되었을 때 idx가 예산을 지급해줄 수 있는 부서의 개수가 됨
}
