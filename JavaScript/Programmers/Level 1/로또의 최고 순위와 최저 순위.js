// lottos 배열에서 0의 개수와 맞은 번호의 개수를 각각 셈
// 맞은 번호와 0의 개수를 더하면 최고 순위, 맞은 번호가 최저 순위가 됨

function solution(lottos, win_nums) {
    const win = [6, 6, 5, 4, 3, 2, 1]; // 6 ~ 1등까지를 나타내는 배열
    
    const count = lottos.filter(lotto => !lotto).length; // filter 메소드를 이용하여 0인 요소를 필터링 후 길이를 구함, !lotto가 0인 경우를 나타냄
    // filter 메소드를 이용하여 맞은 번호의 요소만 필터링 후 길이를 구함, includes 메소드를 이용하여 번호가 포함되어 있는지 확인
    const answer = lottos.filter(lotto => win_nums.includes(lotto)).length;
    return [win[answer + count], win[answer]]; // answer + count가 최고 순위가 되므로 win 배열에서 해당하는 요소 뽑음, answer가 최저 순위가 되므로 win 배열에서 해당하는 요소 뽑음
}
