// 문자열 배열은 순회하면서 +, -에 따라서 분기 처리 후 계산
// class Solution {
//     fun solution(my_string: String): Int {
//         val strings = my_string.split(" ")
//         var answer = 0
//         // 이전의 operator을 기억하기 위한 변수
//         var op = "+"
//         for (str in strings) {
//             val tmp = str.toIntOrNull()
//             if (tmp == null) {
//                 op = str
//                 continue
//             }
//             answer = calculate(x = answer, y = tmp, op = op)
//         }
        
//         return answer
//     }
//     // +, -에 따라 계산해주는 함수
//     private fun calculate(x: Int, y: Int, op: String): Int {
//         return when (op) {
//             "+"  -> x + y
//             "-"  -> x - y
//             else -> 0
//         }
//     }
// }

// replace 메소드를 이용하여 +, - 값을 적절하게 바꾸고 계산
class Solution {
    fun solution(my_string: String): Int {
        return my_string
            .replace("+ ", "")
            .replace("- ", "-")
            .split(" ")
            .sumOf { it.toInt() }
    }
}
