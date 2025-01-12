// class Solution {
//     fun solution(t: String, p: String): Long {
//         var answer = 0L
//         for (i in 0..(t.length - p.length)) {
//             val current = t.slice(i until i + p.length).toLong()
//             if (current <= p.toLong()) answer += 1
//         }
//         return answer
//     }
// }

class Solution {
    fun solution(t: String, p: String): Int {
        return (0..(t.length - p.length))
            .map { t.slice(it until it + p.length) }
            .count { it <= p }
    }
}