// 주어진 score를 평균의 배열로 변환
// 변환 한 배열을 순회하면서 오름차순 정렬된 score 배열에서 현재 값의 index를 구하여 등수를 구해냄
// class Solution {
//     fun solution(score: Array<IntArray>): IntArray {
//         val scoresOfAvg = score.map { it.sum().toDouble() / 2 }
//         val sortedScores = scoresOfAvg.sorted()
//         val scoresSize = scoresOfAvg.size
//         return scoresOfAvg
//             .map {
//                 val count = scoresOfAvg.count { score -> score == it }
//                 scoresSize - sortedScores.indexOf(it) - (count - 1)
//             }
//             .toIntArray()
//     }
// }

// average 메소드를 이용하여 평균을 구하고,
// count 메소드를 이용하여 현재 값의 등수를 구함
class Solution {
    fun solution(score: Array<IntArray>): IntArray {
        val scores = score.map { it.average() }
        return scores
            .map { score -> scores.count { it > score } + 1 }
            .toIntArray()
    }
}
