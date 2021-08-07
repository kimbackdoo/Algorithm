// js에서 forEach 메소드를 이용하여 빈 배열을 순회하는 경우 즉, [].forEach()인 경우 배열의 요소가 없으므로 forEach 메소드 실행 안됨

// 첫번째 인수로 배열을 받고, 두번째 인수로 몇 개를 뽑을지 숫자를 받음, nums의 모든 요소를 순회하면서 조합 배열을 구함
// 예를들어, nums가 [1, 2, 3, 4], pick이 3이라면 1부터 4까지 차례대로 조합을 구함
// 1을 뽑고, 2, 3, 4 중 2개를 뽑음, 2를 뽑고, 3, 4 중 1개를 뽑음
// 재귀적으로 호출하므로 [3], [4]가 return되고, [2, 3], [2, 4]가 return되고, 최종적으로 [1, 2, 3], [1, 2, 4]가 return
// 2을 뽑고, 3, 4 중 2개를 뽑음, 3을 뽑고, 4 중 1개를 뽑음
// [4]가 return되고, [3, 4]가 return되고, 최종적으로 [2, 3, 4]가 return
// 2을 뽑고, 4을 뽑을 경우에는 빈 배열([])에서 1개를 뽑아야 하므로 []가 return 되는데 빈 배열이므로 forEach 메소드가 실행 안됨
// 즉, 위와 같이 3개가 뽑혀야 하는데 2개만 뽑히는 경우는 result에 담기지 않음, 따라서 3개가 뽑히지 않는 경우는 없음 

function combinations(nums, pick) {
    const result = []; // 최종 조합 배열을 담을 배열
    
    if (pick === 1) { // 1개를 뽑는 경우
        return nums.map(num=> [num]); // 배열에서 모든 숫자를 [num]로 변환하여 return
    }
    
    nums.forEach((fixed, idx)=> { // nums의 모든 요소 순회
        const new_nums = nums.slice(idx + 1); // fixed 된 요소를 제외한 나머지 요소 slice
        const combination = combinations(new_nums, pick - 1); // 위와 같이 재귀적으로 조합 배열 구함              
        combination.forEach(item=> result.push([fixed, ...item])); // result에 모든 조합 배열 push
    });
    
    return result;
}
