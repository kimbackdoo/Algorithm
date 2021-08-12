// 1번 수포자는 1, 2, 3, 4, 5, ... 5개가 반복됨
// 2번 수포자는 2, 1, 2, 3, 2, 4, 2, 5, ... 8개가 반복됨
// 3번 수포자는 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ... 10개가 반복됨
// answers에서 1번 수포자부터 차례대로 맞은 개수를 구하면 됨

function solution(answers) {
    const gg = [
        [1, 2, 3, 4, 5], // 1번 수포자
        [2, 1, 2, 3, 2, 4, 2, 5], // 2번 수포자
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] // 3번 수포자
    ];
    
    const answer = gg.map(pattern => // 1, 2, 3번 수포자가 맞은 개수를 구함
                        // answers의 현재 인덱스와 각 수포자의 패턴 길이를 나눈 나머지를 answers의 현재값과 비교하면 됨
                        answers.filter((correct, i) => pattern[i % pattern.length] === correct).length
    );
    // answer의 최대값과 각 수포자의 값이 같으면 인덱스 + 1, 같지 않으면 -1로 매핑 후 0보다 큰 수포자들만 필터링
    return answer.map((n, i) => n === Math.max(...answer) ? i + 1 : -1).filter(n => n > 0);
}
