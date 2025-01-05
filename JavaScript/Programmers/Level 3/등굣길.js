// function solution(m, n, puddles) {
//     const dp = Array.from({ length: n + 1 }, () => Array(m + 1).fill(1))
    
//     puddles.forEach(([pm, pn]) => {
//         dp[pn][pm] = 0
//         if (pn === 1) {
//             for (let j = pm; j <= m; j++) dp[1][j] = 0
//         }
//         if (pm === 1) {
//             for (let i = pn; i <= n; i++) dp[i][1] = 0
//         }
//     })
    
//     for (i = 2; i <= n; i++) {
//         for (j = 2; j <= m; j++) {
//             if (dp[i][j] === 0) continue
//             dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1_000_000_007
//         }
//     }
    
//     return dp[n][m]
// }

function solution(m, n, puddles) {
    const dp = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0))
    puddles.forEach(([pm, pn]) => dp[pn][pm] = -1)
    
    dp[1][1] = 1
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= m; j++) {
            if ((i === 1 && j === 1) || dp[i][j] === -1) continue
            
            if (dp[i][j - 1] > 0) dp[i][j] += dp[i][j - 1] % 1_000_000_007
            if (dp[i - 1][j] > 0) dp[i][j] += dp[i - 1][j] % 1_000_000_007
        }
    }
    
    return dp[n][m] % 1_000_000_007
}
