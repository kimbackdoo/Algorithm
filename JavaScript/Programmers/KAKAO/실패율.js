// 문제 요구에 맞게 구현, 문제 잘 읽을 것!!!
// 스테이지에 도달한 유저가 없는 경우 즉, 분자 또는 분모가 0인 경우 해당 스테이지의 실패율은 0
// // 나누기 연산이 있으므로 항상 분모가 0인 경우 확인해야함

// function solution(N, stages) {
//     const answer = [];
//     for (let i = 1; i <= N; i++) { // 1번부터 N번 스테이지까지 반복
//         stages = stages.filter(stage => stage >= i); // 스테이지 번호가 i보다 크거나 같은 경우 필터링
//         const player = stages.filter(stage => stage === i).length; // 필터링 된 배열에서 스테이지 번호가 i와 같은 경우 필터링 후 길이를 구함
//         const total = stages.length; // 스테이지에 도달한 플레이어 수를 구함
//         const fail = !total ? 0 : player / total; // 분모가 0일 경우 실패율 0
//         answer.push([fail, i]); // [실패율, 스테이지 번호] push
//     }
//     // 실패율을 기준으로 내림차순, 실패율이 같다면 스테이지 번호를 기준으로 오름차순 정렬, 이후 스테이지 번호만 남겨둠
//     return answer.sort((a, b) => (b[0] - a[0]) ? b[0] - a[0] : a[1] - b[1]).map(stage => stage[1]);
// }

// 매번 filter 메소드를 호출하는 것이 아닌 stages를 오름차순 정렬 후 현재 스테이지 번호의 인덱스를 기억하는 방법으로 수정

// function solution(N, stages) {
//     stages.sort((a, b) => a - b); // stages 오름차순 정렬
//     const answer = [];
//     let idx = 0;
//     for (let i = 1; i <= N; i++) {
//         const total = stages.length - idx; // total은 stages의 길이에서 idx를 빼면 됨
//         let player = 0;
//         for (let j = idx; j < stages.length; j++) { // stages를 매번 반복하는 것이 아닌 현재 스테이지 번호에 해당하는 idx부터 반복
//             if (stages[j] > i) { // stages[j]가 i보다 클 경우 break
//                 break;
//             }
//             player++; // player 수 count
//             idx++; // idx count
//         }
        
//         const fail = !total ? 0 : player / total // total이 0일 경우 0, 아닐 경우 실패율을 구함
//         answer.push([fail, i]);
//     }
//     // answer은 이미 스테이지 번호를 기준으로 오름차순 되어 있으므로 실패율 기준으로 내림차순 정렬하면 실패율이 같을 경우에는 오름차순 정렬이 되어 있음
//     return answer.sort((a, b) => b[0] - a[0]).map(stage => stage[1]);
// }

function solution(N, stages) {
    stages.sort((a, b) => a - b);
    const failRate = [];
    let idx = 0;
    for (let i = 1; i <= N; i++) {
        const total = stages.length - idx;
        let player = 0;
        for (let j = idx; j < stages.length; j++) {
            if (stages[j] > i) {
                break;
            }
            player++;
            idx++;
        }
        
        const fail = !total ? 0 : player / total;
        failRate.push(fail);
    }
    
    const tmp = failRate.slice(); // slice 메소드를 이용하여 failRate 배열 복사, 단순히 대입 연산자로 복사하면 참조값이 같기 때문에 둘 중 하나만 바뀌어도 둘 다 바뀌게됨
    return tmp.sort((a, b) => b - a) // 실패율 기준으로 내림차순
        .reduce((answer, fail) => { // 정답 배열을 만들기 위해 reduce 메소드 이용
        answer.push(failRate.indexOf(fail) + 1); // failRate 배열에서 해당 실패율의 인덱스를 찾고 + 1의 값을 answer push
        failRate[failRate.indexOf(fail)] = 2; // 실패율을 아무리 커도 1이므로 방문 처리를 하기 위해 해당 실패율의 값을 2로 변경
        return answer;
    }, []);
}
