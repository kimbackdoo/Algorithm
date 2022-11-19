// 문제에서 주어진대로 slice 하면 됨

// import kotlin.math.min

// class Solution {
//     fun solution(my_str: String, n: Int): Array<String> {
//         val myStrLength = my_str.length
//         val answer = mutableListOf<String>()
//         // step n 만큼 my_str 순회
//         for (start in my_str.indices step n) {
//             // start + min, myStrLength 중 작은값 저장
//             val end = min(start + n, myStrLength)
//             // my_str slicing
//             val slicedMyStr = my_str.slice(start until end)
//             answer.add(slicedMyStr)
//         }

//         return answer.toTypedArray()
//     }
// }

// chunked 메소드 이용하여 n개씩 split
class Solution {
    fun solution(my_str: String, n: Int): Array<String> {
        val answer = my_str.chunked(n)
        return answer.toTypedArray()
    }
}
