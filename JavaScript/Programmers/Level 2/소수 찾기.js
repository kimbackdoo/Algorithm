// numbers로 만들 수 있는 모든 경우를 탐색하고 해당 숫자가 소수인지 아닌지 확인한다.
// dfs 알고리즘을 이용하여 numbers로 만들 수 있는 경우 탐색

function solution(numbers) {
    function isPrime(num) { // 해당 숫자가 소수인지 아닌지 확인하는 함수
        if (num === 0 || num === 1) return false; // num이 0이거나 1일 경우 소수가 아니므로 return false
        
        for (let i = 2; i <= num ** 0.5; i++) { // 해당 숫자가 소수인지 아닌지 확인할 때 num의 제곱근까지만 확인해보면 됨
            if (!(num % i)) return false; // 중간에 나누어 떨어지는 숫자가 있으면 소수가 아니므로 return false
        }
        
        return true; // 소수일 경우 true return
    }
    
    function dfs(p, depth) { // dfs 구현
        if (depth === numbers.length) return; // depth가 numbers의 길이와 같다면 재귀 탈출
        
        // p가 "011", "11"일 경우는 같은 경우이므로 p를 int형으로 바꾸어 확인
        // 숫자가 중복될 수 있으므로 객체를 이용하여 p가 중복되는지 안되는지 확인, 만약 중복이 안된다면
        if (!(+p in check)) {
            check[+p] = 1; // check 객체의 key를 p, value를 1로 체크하여 방문 표시
            if (isPrime(+p)) answer++; // p가 소수라면 count
        }
        
        for (let i = 0; i < numbers.length; i++) { // numbers의 요소로 만들 수 있는 모든 경우를 탐색하기 위해 numbers 순회
            if (!visited[i]) { // i번째 요소 방문하지 않았으면
                visited[i] = true; // 방문 처리
                dfs(p + numbers[i], depth); // dfs 탐색
                visited[i] = false; // 방문 처리 취소
            }
        }
    }
    
    const check = {}; // 해당 숫자가 중복되는지 확인하기 위한 객체
    const visited = new Array(numbers.length).fill(false); // 방문 여부를 확인할 배열, new Array를 이용하여 numbers의 길이만큼 배열을 만들고, fill 메소드를 이용하여 false를 채워넣음
    let answer = 0;
    dfs("", 0); // dfs 탐색
    return answer;
}
