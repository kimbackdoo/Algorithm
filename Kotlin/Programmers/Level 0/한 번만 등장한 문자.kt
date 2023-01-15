// 주어진 문자열에서 문자마다 카운팅 후 개수가 1개인 요소들만 모아서 오름차순 정렬 후 return
// class Solution {
//     fun solution(s: String): String {
//         val tmp = s.toSortedSet()
//         var answer = ""
//         tmp.forEach { el ->
//             val cnt = s.count { it == el }
//             if (cnt == 1) answer += el
//         }
//         return answer
//     }
// }

// 함수형 프로그래밍으로 풀이
class Solution {
    fun solution(s: String): String {
        return s.toSortedSet()
            .filter { el -> s.count { el == it } == 1 }
            .joinToString("")
    }
}
