// "(", ")"의 개수가 똑같은지 확인하면 됨, stack 사용

function solution(s){
    const answer = [];
    for (let b of s) { // s 문자열 모든 요소 순회
        if (answer.length && answer[answer.length - 1] === "(" && b === ")") { // answer이 비어있지 않고, answer의 마지막 요소가 "(", b가 ")"면 짝이 맞는 것이므로
            answer.pop(); // pop 연산
            continue; // continue
        }
        
        if (b === ")") { // 괄호 시작이 ")"로 시작한다면 false return
            return false;
        }
        
        answer.push(b); // "(" push
    }
    
    return answer.length ? false : true; // answer가 비어있지 않으면 false, 비어있으면 true return
}
