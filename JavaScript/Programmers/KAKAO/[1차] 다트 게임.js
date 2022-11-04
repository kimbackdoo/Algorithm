// 문제 요구에 맞게 구현하면 됨

function solution(dartResult) {
    const bonus = {S: 1, D: 2, T: 3}; // 보너스 점수 객체
    const option = {"*": 2, "#": -1}; // 옵션 점수 객체
    
    let num = ""; // 0 ~ 10까지의 점수를 처리하기 위해 문자열
    const answer = []; // 결과값을 담을 배열
    for (let dart of dartResult) {
        if (!isNaN(dart)) { // dart가 숫자면 num에 dart를 이어나가면 됨
            num += dart;
        } else if (dart in bonus) { // dart가 보너스 점수에 해당한다면 보너스 점수 계산
            answer.push((+num) ** bonus[dart]);
            num = ""; // 점수 초기화
        } else { // dart가 옵션 점수에 해당한다면
            answer[answer.length - 1] *= option[dart]; // 옵션 점수 계산
            if (dart === "*" && answer.length >= 2) { // dart가 "*"이고, answer의 길이가 2 이상이면 점수가 중첩될 수 있으므로 answer의 마지막 두번째 요소 * 2
                answer[answer.length - 2] *= 2;
            }
        }
    }
    
    return answer.reduce((sum, current) => sum + current, 0); // reduce 메소드를 이용하여 점수 계산
}
