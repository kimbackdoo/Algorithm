// 각 기능이 배포될 수 있는 날짜를 구하고 각 기능이 배포될 때 몇 개의 기능과 함께 배포되는지 count

function solution(progresses, speeds) {
    const result = progresses.map((progress, i) => Math.ceil((100 - progress) / speeds[i])); // map 메소드를 이용하여 각 기능이 배포될 수 있는 날짜 구함
    const answer = [1]; // 첫 번째 기능은 무조건 배포되므로 배열 초기값 1로 설정
    let check = result[0]; // 첫 번째 기능은 무조건 배포되므로 비교하기 위한 check 변수의 초기값 result[0]로 설정
    for (let i = 1; i < result.length; i++) { // 첫 번째 기능은 확인하였으므로 2번째 기능부터 반복
        if (check >= result[i]) { // check가 result[i]보다 크거나 같다면 즉, 날짜가 포함된다면
            answer[answer.length - 1]++; // answer의 마지막 요소 1증가
            continue;
        }
        
        check = result[i]; // 날짜가 포함안된다면 즉, result[i]가 check보다 크다면 check 값 갱신
        answer.push(1); // 새로 배포하는 것이므로 answer에 push(1)
    }
    
    return answer;
}
