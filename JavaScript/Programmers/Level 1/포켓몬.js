// 최대한 많은 포켓몬을 선택해야 함, 즉, 중복을 제거해야함, new Set() 사용
// 예를들어, [3, 3, 3, 2, 2, 4]에서 3마리를 선택해야하고, 중복을 제거하면 [3, 2, 4]가 됨, 따라서 3, 2, 4를 선택하면 됨
// 예를들어, [3, 3, 3, 2, 2, 2]에서 3마리를 선택해야하고, 중복을 제거하면 [3, 2]가 됨, 따라서 3, 3, 2 또는 3, 2, 2를 선택할 수 있므로 포켓몬의 종류는 3, 2 2마리가 됨
// 즉, new Set(nums).size와 nums.length / 2의 값 중 작은 값이 선택했을 때 최대한 많은 포켓몬의 종류가 됨

function solution(nums) {
    return Math.min(new Set(nums).size, nums.length / 2); // Math.min을 사용하여 set의 크기와 nums.length / 2 값 중 작은 값을 return
}
