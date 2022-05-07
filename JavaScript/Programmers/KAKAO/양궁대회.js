// 초기 접근까지 많은 시간이 사용한 문제
// 처음에는 어피치보다 점수차를 가장 높게 하기 위해 그리디인줄 알고 접근했지만
// 크기가 11인 배열에서 중복을 포함하여 n개를 뽑는 경우를 구하면 된다는 것을 깨달음
// 즉, 백트래킹 (dfs) 알고리즘 사용

// 최종 가장 큰 점수차와 그때 라이언의 결과를 저장할 배열
const answer = [0, []];

function dfs({ ryanInfo, apeachInfo, n, index, pick }) { // 백트래킹 (dfs) 알고리즘 구현, 매개변수를 확실하게 알기 위해 객체로 선언
    if (pick == n) { // n개 만큼 뽑았으면
        const score = { ryan: 0, apeach: 0 }; // 라이언과 어피치의 점수를 저장할 객체
        for (let i = 1; i < 11; i++) {
            // 현재 라이언의 점수가 0보다 크고, 어피치보다 점수가 높으면 라이언의 점수 count
            if (ryanInfo[i] > 0 && ryanInfo[i] > apeachInfo[i]) score.ryan += i;
            // 현재 어피치의 점수가 0보다 크고, 어피치가 라이언보다 점수가 크거나 같으면 어피치의 점수 count
            else if (apeachInfo[i] > 0) score.apeach += i;
        }
        
        const gap = score.ryan - score.apeach; // 라이언과 어피치의 점수차를 구함
        if (gap > 0 && answer[0] < gap) { // 점수차가 0보다 크고, answer의 점수차보다 gap이 크면
            // answer 값 업데이트
            // 이때, answer[1] = ryanInfo 이렇게 값을 업데이트하면 배열의 얕은 복사가 이루어지므로
            // 원하는 값이 출력안된다.
            // 따라서 deep copy 하거나 전개문법으로 새로운 배열을 업데이트 하는 방식으로 진행
            [answer[0], answer[1]] = [gap, [...ryanInfo]];
        }
        
        return; // 재귀 탈출
    }
    
    // 배열 모든 요소 순회
    // i의 초기값을 index로 하여 중복으로 탐색하지 않게함
    for (let i = index; i < 11; i++) {
        ryanInfo[i] += (apeachInfo[i] + 1); // i번째 요소 방문
        dfs({ ryanInfo, apeachInfo, n, index: i + 1, pick: pick + (apeachInfo[i] + 1) }); // dfs 탐색
        ryanInfo[i] -= (apeachInfo[i] + 1); // i번째 요소 방문 취소
    }
}

function solution(n, info) {
    const ryanInfo = Array(11).fill(0); // 라이언의 초기 배열 선언
    // 점수는 10점부터 시작되므로 info 배열을 뒤집음
    // 뒤집는 이유는 라이언과 어피치의 점수차가 가장 커야하고, 점수차들이 같으면 낮은 점수를 더 많이 맞혀야 하기 때문에
    // 1점부터 탐색하기 위해 info 배열을 뒤집음
    const apeachInfo = info.reverse();
    // 1 ~ 10까지 다 쏘고 화살이 남았으면 0점에 몰아주어야함
    // 따라서 미리 0점의 개수를 정해두고 1점부터 10점의 개수를 탐색
    // 이때, 0점은 어피치가 0점을 맞힌 개수보다 많을 필요 없기 때문에 최대 어피치가 맞힌 개수로 고정시키고 반복문 실행
    for (let i = 0; i <= apeachInfo[0]; i++) {
        ryanInfo[0] = i; // 라이언의 0점 개수 업데이트
        dfs({ ryanInfo, apeachInfo, n: n - i, index: 1, pick: 0 }); // dfs 탐색 시작
    }
    
    // 최종 점수차가 0점이면 무조건 지거나 비기는 경우이기 때문에 [-1]
    // 라이언이 이긴다면, 현재 배열은 0점부터 나열되어 있으므로 reverse 메소드를 이용하여 배열을 뒤집고 return
    return answer[0] ? answer[1].reverse() : [-1];
}
