// 현재 학생이 체육복을 빌려줄 수 있는지 없는지 체크 => 그리디 알고리즘 적용
// 여벌 체육복을 가지고 온 학생이 체육복을 잃어버린 경우는 본인이 입어야 하므로 lost, reserve 배열에서 각각 차집합을 구함
// 학생 번호 -1, +1인 경우에 해당하면 체육복을 빌려줌

function solution(n, lost, reserve) {
    let diffLost = lost.filter(number=> !reserve.includes(number)); // lost와 reserve의 차집합을 구함
    let diffReserve = reserve.filter(number=> !lost.includes(number)); // reserve와 lost의 차집합을 구함
    
    diffReserve.forEach(number=> { // forEach 메소드를 사용하여 diffReserve의 모든 요소를 순회
        if (diffLost.indexOf(number - 1) !== -1) { // number - 1이 diffLost에 있다면
            diffLost.splice(diffLost.indexOf(number - 1), 1); // 체육복을 빌려줌
        } else if (diffLost.indexOf(number + 1) !== -1) { // number + 1이 diffLost에 있다면
            diffLost.splice(diffLost.indexOf(number + 1), 1); // 체육복을 빌려줌
        }
    });
    
    return n - diffLost.length; // 전체 학생 수에서 빌리지 못한 학생 수를 빼면 정답
}
