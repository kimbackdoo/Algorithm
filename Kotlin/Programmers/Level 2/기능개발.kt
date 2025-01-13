import kotlin.math.ceil

// class Solution {
//     fun solution(progresses: IntArray, speeds: IntArray): List<Int> {
//         val deploy = progresses.mapIndexed { index, progress -> ceil((100 - progress) * 1.0 / speeds[index]).toInt() }
//         val answer = mutableListOf<Int>(1)
//         var tmp = deploy[0]
//         for (i in 1 until deploy.size) {
//             if (tmp >= deploy[i]) {
//                 answer[answer.size - 1] += 1
//                 continue  
//             }
//             tmp = deploy[i]
//             answer += 1
//         }

//         return answer
//     }
// }

class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): List<Int> {
        val answer = mutableListOf<Int>()
        var tmp = 0
        for (i in progresses.indices) {
            val deploy = ceil((100 - progresses[i]) * 1.0 / speeds[i]).toInt()
            if (tmp >= deploy) {
                answer[answer.size - 1] += 1
                continue
            }
            tmp = deploy
            answer += 1
        }

        return answer
    }
}