// 스택 자료구조를 이용하여 스택의 마지막 값과 같으면 pop, 아니면 push
// 마지막에 스택이 비어 있으면 1, 아니면 0 return

// function solution(s) {
//     const answer = []; // 짝을 확인할 스택
//     [...s].forEach(w => { // 전개문법을 이용하여 s를 배열로 변환 후, forEach 메소드를 이용하여 s의 모든 요소 순회
//         if (answer.length && answer[answer.length - 1] === w) { // answer가 비어있지 않고, answer의 마지막 값과 w가 같다면
//             answer.pop(); // pop()
//             return; // forEach의 인수는 callback 함수이므로 continue가 아닌 return으로 현재 요소 순회 종료
//         }
        
//         answer.push(w); // 아니라면 answer에 w push
//     });

//     return !answer.length ? 1 : 0; // answer의 길이가 0이라면 1, 아니면 0 return
// }

// s를 배열로 변환하지 않고, for of 문을 이용한다.

function solution(s) {
    const answer = [];
    for (let w of s) { // for of 문을 이용하여 s의 모든 요소 순회
        if (answer.length && answer[answer.length - 1] === w) {
            answer.pop();
            continue;
        }
        
        answer.push(w);
    }

    return !answer.length ? 1 : 0;
}
