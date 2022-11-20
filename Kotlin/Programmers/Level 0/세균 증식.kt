// 시간당 2마리씩 세균 번식
// n = 2, t = 10 일 경우,
// 4 -> 8 -> 16 -> 32 -> 64 -> ... -> 2048 이 됨
// 즉, 공비수열, 공식을 이용하여 t시간 후의 세균 구함

// import kotlin.math.pow

// class Solution {
//     fun solution(n: Int, t: Int): Int {
//         // 공비는 2
//         val r = 2
//         // 등비수열 공식 적용
//         return (n * r.toDouble().pow(t)).toInt()
//     }
// }

// fold 메소드를 이용하여 1 ~ t까지 공비를 곱해나감
class Solution {
    fun solution(n: Int, t: Int): Int {
        val r = 2
        return (1..t).fold(n) { acc, _ -> acc * r }
    }
}
