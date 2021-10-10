// 문제 조건 대로 정렬하면 됨
// 승률은 전체 경기 중에서 이긴 횟수를 구하는 것이므로 아직 경기를 하지 않은 경우라면 승률에 포함되면 안됨

// function solution(weights, head2head) {
//     const answer = [];
//     for (let i = 0; i < weights.length; i++) {
//         let total = 0, win = 0, cnt = 0;
//         for (let j = 0; j < weights.length; j++) {
//             if (head2head[i][j] !== "N") { // 경기를 했다면
//                 total++; // 전체 경기수 count
//                 if (head2head[i][j] === "W") { // 이겼다면
//                     if (weights[i] < weights[j]) { // 본인보다 무거운 복서를 이겼다면
//                         cnt++; // 횟수 count
//                     }
//                     win++; // 이긴 횟수 count
//                 }
//             }
//         }
//         const rate = total ? win / total : 0; // 승률 계산
//         answer.push([rate, cnt, weights[i], i + 1]); // 정렬하기 위해 문제 조건대로 answer에 push
//     }

//     return answer.sort((a, b) => b[0] - a[0] ? b[0] - a[0] : // 문제 조건대로 sort 후 복서의 번호만 남기도록 mapping
//                        b[1] - a[1] ? b[1] - a[1] :
//                        b[2] - a[2] ? b[2] - a[2] : a[3] - b[3])
//         .map(el => el[3]);
// }

// 정렬할 때 삼항 연산자를 사용하지 않고 논리 연산자를 사용하여 가독성 높임
function solution(weights, head2head) {
    const answer = [];
    for (let i = 0; i < weights.length; i++) {
        let total = 0, win = 0, cnt = 0;
        for (let j = 0; j < weights.length; j++) {
            if (head2head[i][j] !== "N") {
                total++;
                if (head2head[i][j] === "W") {
                    if (weights[i] < weights[j]) {
                        cnt++;
                    }
                    win++;
                }
            }
        }
        const rate = total ? win / total : 0;
        answer.push([rate, cnt, weights[i], i + 1]);
    }
    
    return answer.sort((a, b) => b[0] - a[0] || b[1] - a[1] || b[2] - a[2] || a[3] - b[3]) // 논리 연산자를 활용하여 sort
        .map(el => el[3]);
}
