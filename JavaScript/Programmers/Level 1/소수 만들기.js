// 입력받은 배열에서 3개를 뽑아 그 합이 소수인지 아닌지 체크

function check(num) { // 소수 체크
    for (let i = 2; i <= num ** 0.5; i++) { // num의 제곱근까지만 확인하면 되므로 num의 제곱근까지 반복하여 소수 체크
        if (num % i === 0) {
            return false; // 중간에 나눠떨어지는 수가 있으면 소수가 아니므로 false return
        }
    }
    
    return true; // 소수면 true return
}

function combinations(nums, pick) { // 조합
    const result = [];
    
    if (pick === 1) {
        return nums.map(num=> [num]);
    }
    
    nums.forEach((fixed, idx)=> {
        const new_nums = nums.slice(idx + 1);
        const combination = combinations(new_nums, pick - 1);
        combination.forEach(item=> result.push([fixed, ...item]));
    });
    
    return result;
}

function solution(nums) {
    const combination = combinations(nums, 3); // num에서 3개를 뽑아 배열 생성
    const answer = combination.map(c=> c.reduce((sum, current)=> sum + current, 0)); // reduce 메소드를 이용하여 뽑힌 조합 배열의 모든 요소를 합으로 만듦 
    return answer.filter(num=> check(num)).length; // filter 메소드를 이용하여 소수인 숫자만 배열에 남기고 그 길이를 return
}
