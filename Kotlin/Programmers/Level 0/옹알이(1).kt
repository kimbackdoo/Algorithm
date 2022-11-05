// 코틀린 언어가 익숙하지 않아 한참을 돌고 돌아 푼 문제...
// 계속 사용하려고 노력해야할듯
// 옹알이 발음이 될 수 있는 모든 경우의 수를 구하고,
// 주어진 발음이 이미 구한 경우들에 포함되는지 확인

// class Solution { 
//     var result = arrayOf<String>()
    
//     fun dfs(list: Array<String>, visited: Array<Boolean>, cases: String) {
//         for (i in list.indices) {
//             if (!visited[i]) {
//                 visited[i] = true
//                 dfs(list, visited, "${cases}${list[i]}")
//                 visited[i] = false
//             }
//         }

//         result += cases
//     }
    
//     fun solution(babbling: Array<String>): Int {
//         val possibleBabbling = arrayOf("aya", "ye", "woo", "ma")
//         val visited = Array(possibleBabbling.size) { false }
//         dfs(possibleBabbling, visited, "")

//         var answer = 0
//         for (b in babbling) {
//             if (result.contains(b)) answer++
//         }

//         return answer
//     }
// }

// replace 메소드를 이용하여 가능한 옹알이 발음을 "."로 변환
// 이후 "."의 개수가 현재 발음의 개수와 같다면 카운팅
class Solution { 
    fun solution(babbling: Array<String>): Int {
        val possibleBabbling = arrayOf("aya", "ye", "woo", "ma")
        var answer = 0
        for (i in babbling.indices) {
            for (pb in possibleBabbling) {
                babbling[i] = babbling[i].replace(pb, ".")
            }

            val length = babbling[i].filter { it == '.' }.length
            val isPossible = length == babbling[i].length
            if (isPossible) answer++
        }

        return answer
    }
}
