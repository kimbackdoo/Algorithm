// 2중 for문으로 문제를 풀면 시간초과
// number의 앞에서부터 탐색을 진행하면서 그때그때마다 값이 큰지 작은지 선택해야함, 그리디 알고리즘 적용

function solution(number, k) {
    const answer = [];
    // number의 모든 요소 순회
    for (let num of number) {
        // k가 0 보다 크고, 현재 값이 answer의 마지막 값보다 크면
        // 즉, 더 큰 수를 만들 수 있으면
        while (k && +num > +answer[answer.length - 1]) {
            answer.pop(); // pop 연산 진행
            k--; // k값 감소
        }
        
        answer.push(num) // 모든 num의 값 answer에 push
    }
    
    // 만약 k의 값이 0보다 크다면 answer에서 뒤에서 k만큼 잘라내고 문자열로 변환 후 return
    return answer.slice(0, answer.length - k).join("");
}
