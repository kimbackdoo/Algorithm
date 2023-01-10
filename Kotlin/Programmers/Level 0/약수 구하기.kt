// 약수는 자신의 제곱근까지의 반복으로 모두 구할 수 있음
// import kotlin.math.sqrt

// class Solution {
//     fun solution(n: Int): IntArray {
//         val answer = mutableListOf(1, n)
//         for (num in 2..sqrt(n.toDouble()).toInt()) {
//             if (n % num != 0) continue
//             answer += num
//             answer += n / num
//         }

//         return answer.toSet().sorted().toIntArray()
//     }
// }

// 단순히 1 ~ n까지 반복하면서 나누어 떨어지는 수를 찾으면 됨
class Solution {
    fun solution(n: Int): IntArray {
        return (1..n).filter { n % it == 0 }.toIntArray()
    }
}
