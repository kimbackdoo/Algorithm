// 문제에서는 단순히 X 연산자 Y = Z 형식이라고 했지만 조금 더 확장시켜서 풀기 위해 고민을 했던 문제

// class Solution {
//     fun solution(quiz: Array<String>): Array<String> {
//         val answer = mutableListOf<String>()
//         // quiz 모든 요소 순회
//         quiz.forEach { str ->
//             // str split 후 trim
//             val (expr, result) = str.split("=").map { it.trim() }
//             // expr 을 공백을 기준으로 split -> [숫자, 연산자, 숫자] 형식이 됨
//             val ops = expr.split(" ").toMutableList()
//             var tmp = 0
//             var index = 0
//             while (index < ops.size) {
//                 // ops의 처음 요소부터 순회
//                 val op = ops[index++]
//                 tmp += when (op) {
//                     // +면 다음 숫자 더해줌
//                     "+"  -> ops[index++].toInt()
//                     // -면 다음 숫자 빼줌
//                     "-"  -> -ops[index++].toInt()
//                     // 숫자면 해당 숫자 더해줌
//                     else -> op.toInt()
//                 }
//             }
//             val isAnswer = tmp == result.toInt()
//             answer += if (isAnswer) "O" else "X"
//         }
//         return answer.toTypedArray()
//     }
// }

// 단순히 공백을 기준으로 split 후 비교
class Solution {
    fun solution(quiz: Array<String>): Array<String> {
        val answer = mutableListOf<String>()
        for (q in quiz) {
            val (x, op, y, _, z) = q.split(" ")
            answer += when (op) {
                "+"  -> if (x.toInt() + y.toInt() == z.toInt()) "O" else "X"
                else -> if (x.toInt() - y.toInt() == z.toInt()) "O" else "X"
            }
        }
        return answer.toTypedArray()
    }
}
