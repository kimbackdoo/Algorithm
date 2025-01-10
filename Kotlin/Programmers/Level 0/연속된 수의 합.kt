// 처음에는 (total / num) - 2 ~ (total / num) 까지 순회하면서 연속수의 합이 total이 되는지 확인하였지만 오답
// num이 홀수인지 짝수인지에 따라 초기 배열을 나누고
// 배열의 첫번째값, 마지막값을 기준으로 값을 추가하여 계산

// import kotlin.math.floor

// class Solution {
//    fun solution(num: Int, total: Int): IntArray {
//        // num이 홀수인지 짝수인지 확인
//        val isOdd = num % 2 != 0
//        // 중간값 구함
//        val middle = floor((total / num).toDouble()).toInt()
//        // num이 홀수면 배열에 중간값만 넣고, 짝수면 중간값, 중간값 + 1을 넣음
//        val answer = if (isOdd) mutableListOf<Int>(middle) else mutableListOf<Int>(middle, middle + 1)
//        // answer의 크기가 num보다 작은 경우만 순회
//        while (answer.size < num) {
//            // answer에서 첫번째 값, 마지막 값을 각각 구함
//            val first = answer.first()
//            val last = answer.last()
//            // 첫번째값 - 1을 배열 첫번째에 add
//            answer.add(0, first - 1)
//            // 마지막값 + 1을 배열 마지막에 add
//            answer.add(last + 1)
//        }
//        // answer을 intArray로 형변환하여 return
//        return answer.toIntArray()
//    }
// }

// 등차수열 공식 이용
// s = n * (2 * a + (n - 1) * d) / 2
// s -> total, n -> num, d -> 1
fun solution(num: Int, total: Int): IntArray {
    val start = ((2 * total) / num + 1 - num) / 2
    return IntArray(num) { i -> i + start }
}